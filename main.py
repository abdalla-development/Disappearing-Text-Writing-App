from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap

start_text = ""


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/type", methods=["POST", "GET"])
def typing():
    global start_text
    if request.method == "GET":
        return render_template("type.html", text=start_text)
    elif request.method == "POST":
        text = request.form["textarea"]
        print(text)
        if start_text == text:
            start_text = ""
        else:
            start_text = text
        return render_template("type.html", text=start_text)


if __name__ == "__main__":
    app.run(debug=True)
