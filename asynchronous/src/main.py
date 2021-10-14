from flask import Flask, render_template, request
from UserModel import User
from setting import session
from sqlalchemy import *
from sqlalchemy.orm import *

app = Flask(__name__)

@app.route("/", methods=["POST"])
def register_record():
    name = request.form["name"]
    session.add(User(name))
    session.commit()
    return render_template("hello.html", name=name, message="登録完了しました!")

@app.route("/", methods=["GET"])
def fetch_record():
    name = request.args.get("name")
    db_user = session.query(User.name).filter(User.name == name).all()

    if len(db_user) == 0:
        message = "登録されていません｡"
    else:
        message = "登録されています｡"

    return render_template("hello.html", name=name, message=message)

@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run()