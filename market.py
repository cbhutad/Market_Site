from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index_home_page():
    return render_template("index.html")