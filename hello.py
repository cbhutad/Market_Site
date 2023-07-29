from flask import Flask 
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.get("/user/<username>")
def user_details(username="Dummy User"):
    return f"<h1> This page details the info about user : {escape(username)}</h1>"