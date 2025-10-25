from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    name = request.args.get("name", "User")
    return f"Hello, {escape(name)}!"


@app.route("/user/<username>")
def getUser(username):
    return f"Hello, {escape(username)}!"

