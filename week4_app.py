from flask import Flask 
from flask import request
from flask import render_template
from flask import redirect
app=Flask(__name__,static_folder="static",static_url_path="/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member/")
def member():
    return render_template("member.html")

@app.route("/error/")
def error():
    return render_template("error.html")

@app.route("/signin")
def signin():
    user=request.args.get("user")
    password=request.args.get("password")
    if user=="test" and password=="test":
        return redirect("/member")
    else:
        return redirect("/error")

app.run(debug=True,port=3000) 