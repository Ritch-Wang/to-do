import json
from todo_api import TodoAPI

api = TodoAPI()

def lambda_handler(event, context):
    def response(status, body):
        return {
            "statusCode": status,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(body)
        }

    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")
    payload = {}

    if event.get("body"):
        try:
            payload = json.loads(event.get("body"))
        except Exception:
            return response(400, {"message": "Invalid JSON body"})

    if method == "GET":
        return response(200, api.get_list())

    elif method == "POST":
        title = payload.get("title")
        if not title:
            return response(400, {"message": "Missing 'title'"})

        return response(201, api.add_item(title))

    elif method == "DELETE":
        item_id = payload.get("id")
        if item_id is None:
            return response(400, {"message": "Missing 'id'"})

        deleted = api.delete_item(item_id)
        if deleted is None:
            return response(404, {"message": "Todo not found"})

        return response(200, deleted)

    else:
        return response(405, {"message": "Method not allowed"})