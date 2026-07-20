from dotenv import load_dotenv
load_dotenv()  # reads DATABASE_URL from .env before TodoAPI connects

from flask import Flask, jsonify, request
from todo_api import TodoAPI

app = Flask(__name__)
api = TodoAPI()


@app.route("/list", methods=["GET"])
def get_list_route():
    return jsonify(api.get_list())


@app.route("/list", methods=["POST"])
def add_item_route():
    payload = request.get_json(force=True) or {}
    title = payload.get("title")
    if not title:
        return jsonify({"message": "Missing 'title'"}), 400
    return jsonify(api.add_item(title)), 201


@app.route("/list/<int:item_id>", methods=["DELETE"])
def delete_item_route(item_id):          # id comes from the URL
    deleted = api.delete_item(item_id)
    if deleted:
        return jsonify({"deleted": deleted}), 200
    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)