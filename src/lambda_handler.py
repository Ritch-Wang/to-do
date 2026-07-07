import json
from todo_api import TodoAPI

api = TodoAPI()

def lambda_handler(event, context):
    path = event.get("rawPath", "/")

    if path == "/list":
        return api.get_list()

    elif path == "/add":
        body = json.loads(event.get("body") or "{}")
        title = body.get("title")
        return api.add_item(title)

    elif path == "/delete":
        body = json.loads(event.get("body") or "{}")
        item_id = body.get("id")
        return api.delete_item(item_id)

    return {
        "statusCode": 404,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"error": "Not found"})
    }