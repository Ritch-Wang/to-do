from flask import Flask

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def list_route():
    return {"message": "hello_world"}

if __name__ == '__main__':
    app.run(debug=True)