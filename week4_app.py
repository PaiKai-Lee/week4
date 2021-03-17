from flask import Flask 
from flask import request
from flask import render_template
app=Flask(__name__,static_folder="static",static_url_path="/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/error")
def error():
    return render_template("error.html")

app.run(port=3000) 