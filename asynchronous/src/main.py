from flask import Flask, request
from UserModel import User
from setting import session
from sqlalchemy import *
from sqlalchemy.orm import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def register_record():
    name = request.form["name"]
    session.add(User(name))
    session.commit()
    message = name + "の登録が完了しました!"

    return message

@app.route("/", methods=["GET"])
def fetch_record():
    name = request.args.get("name")
    db_user = session.query(User.name).filter(User.name == name).all()

    if len(db_user) == 0:
        message = "登録されていません｡"
    else:
        message = "登録されています｡"

    return str(name) + message

if __name__ == "__main__":
    app.run()