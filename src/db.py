import os
import psycopg


class Database:
    def __init__(self):
        self.conn = psycopg.connect(
            host=os.environ["DB_HOST"],
            port=5432,
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )

    def get_all_todos(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id, title
                FROM todos
                ORDER BY id;
            """)
            return cur.fetchall()

    def add_todo(self, title):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO todos(title)
                VALUES (%s)
                RETURNING id, title;
            """, (title,))
            row = cur.fetchone()
            self.conn.commit()
            return row

    def delete_todo(self, item_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM todos
                WHERE id = %s
                RETURNING id;
            """, (item_id,))
            row = cur.fetchone()
            self.conn.commit()
            return row