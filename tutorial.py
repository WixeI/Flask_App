from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, employees=["Tim", "John", "Ann"])

@app.route("/mine/")
def mine():
    return redirect("https://www.youtube.com/watch?v=0KvlwMd3C4Y")

if __name__ == "__main__":
    app.run(debug = True)

