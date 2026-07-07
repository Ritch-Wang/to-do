import json
from db import Database

class TodoAPI:
    def __init__(self):
        self.db = Database()

    def _response(self, status_code, body):
        return {
            "statusCode": status_code,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(body)
        }

    def get_list(self):
        try:
            todos = self.db.get_all_todos()

            result = {
                "todos": [
                    {"id": row[0], "title": row[1]}
                    for row in todos
                ]
            }

            return self._response(200, result)

        except Exception as e:
            return self._response(500, {"error": str(e)})

    def add_item(self, title):
        try:
            row = self.db.add_todo(title)

            if row is None:
                return self._response(400, {"error": "Failed to add todo"})

            return self._response(201, {
                "id": row[0],
                "title": row[1]
            })

        except Exception as e:
            return self._response(500, {"error": str(e)})

    def delete_item(self, item_id):
        try:
            row = self.db.delete_todo(item_id)

            if row is None:
                return self._response(404, {"error": "Todo not found"})

            return self._response(200, {
                "id": row[0]
            })

        except Exception as e:
            return self._response(500, {"error": str(e)})