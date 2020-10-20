import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    """Method 1: Return a simple hello"""
    return "Hello", 200


@app.route("/hello/<my_name>", methods=["GET"])
def hello_name(my_name):
    """Method 2: Return hello with name, given in url"""
    return f"Hello from url, {my_name}", 200


@app.route('/foo', methods=['POST']) 
def foo():
    data = request.json
    return jsonify(data)
# curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "fizz bizz"}' http://localhost:8080/foo


@app.route("/")
def top_page():
    """top_page"""
    return "Welcome to my application, version 1\n"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))