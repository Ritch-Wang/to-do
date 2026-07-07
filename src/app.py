from flask import Flask, jsonify, request
from todo_api import TodoAPI

app = Flask(__name__)
api = TodoAPI()

@app.route("/list", methods=["GET"])
def get_list_route():
    return jsonify(api.get_list())

@app.route("/add", methods=["POST"])
def add_item_route():
    data = request.get_json()
    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400
    return jsonify(api.add_item(title))

@app.route("/delete", methods=["DELETE"])
def delete_item_route():
    data = request.get_json()
    item_id = data.get("id")
    if item_id is None:
        return jsonify({"error": "id is required"}), 400
    result = api.delete_item(item_id)
    if result is None:
        return jsonify({"error": "item not found"}), 404
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=8000, debug=True)