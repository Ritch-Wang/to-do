import os
import json
from urllib.parse import urlparse
import pg8000.dbapi


def _load_db_config():
    # Local dev: parse DATABASE_URL from .env / docker-compose.
    if os.environ.get("DATABASE_URL"):
        parsed = urlparse(os.environ["DATABASE_URL"])
        return {
            "user": parsed.username,
            "password": parsed.password,
            "host": parsed.hostname,
            "port": parsed.port or 5432,
            "database": parsed.path.lstrip("/"),
        }

    # Production (Lambda): pull credentials from Secrets Manager instead.
    secret_name = os.environ["DB_SECRET_NAME"]
    import boto3  # already bundled in the Lambda runtime, no need to zip it
    client = boto3.client("secretsmanager")
    secret = json.loads(client.get_secret_value(SecretId=secret_name)["SecretString"])
    return {
        "user": secret["username"],
        "password": secret["password"],
        "host": secret["host"],
        "port": secret["port"],
        "database": secret["dbname"],
    }


def _rows_as_dicts(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


class TodoAPI:
    def __init__(self):
        # Same config shape works for local Docker and RDS -
        # only where it's sourced from changes (env var vs Secrets Manager).
        self.db_config = _load_db_config()

    def _get_connection(self):
        return pg8000.dbapi.connect(**self.db_config)

    def get_list(self):
        conn = self._get_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, title FROM todos ORDER BY id;")
            result = {"todos": _rows_as_dicts(cur)}
            cur.close()
            return result
        finally:
            conn.close()

    def add_item(self, title):
        conn = self._get_connection()
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO todos (title) VALUES (%s) RETURNING id, title;",
                (title,)
            )
            new_todo = _rows_as_dicts(cur)[0]
            conn.commit()
            cur.close()
            return new_todo
        finally:
            conn.close()

    def delete_item(self, item_id):
        conn = self._get_connection()
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM todos WHERE id = %s RETURNING id, title;",
                (item_id,)
            )
            rows = _rows_as_dicts(cur)
            conn.commit()
            cur.close()
            return rows[0] if rows else None
        finally:
            conn.close()