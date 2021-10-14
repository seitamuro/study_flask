from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return render_template("hello.html", name=name, method="URLパラメータ")

@app.route("/param", methods=["GET", "POST"])
def hello_world_with_parameter():
    if request.method == "POST":
        name = request.form["name"]
    else:
        name = request.args.get("name")

    return render_template("hello.html", name=name, method=request.method)

@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run()