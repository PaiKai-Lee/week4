from flask import Flask,request,render_template,redirect,session

app=Flask(__name__,static_folder="static",static_url_path="/")
app.secret_key=b'\xc5\xde%\xf9\x1e@\r\x90\x17\x10\xd7\xc5\x08\x94\x9b\r'

@app.route("/")
def index():
    if "user" in session:
        return redirect("/member/")
    else:
        return render_template("index.html")

@app.route("/member/")
def member():
    if "user" in session:
        return render_template("member.html")
    else:
        return redirect("/")
@app.route("/error/")
def error():
    return render_template("error.html")

@app.route("/signin",methods=["POST"])
def signin():
    user=request.form["user"]
    password=request.form["password"]
    if user=="test" and password=="test":
        session["user"]=user
        session.permanent= True
        return redirect("/member")
    else:
        return redirect("/error")
@app.route("/signout")
def signout():
    session.pop("user",None)
    return redirect("/")

app.run(port=3000) 