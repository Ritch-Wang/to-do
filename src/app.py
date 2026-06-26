from flask import Flask, jsonify
from todo_api import TodoAPI

app = Flask(__name__)
api = TodoAPI()

@app.route("/list", methods=["GET"])
def get_list_route():
    return jsonify(api.get_list())