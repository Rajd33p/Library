from flask import Flask, render_template, url_for
from features import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", data=B_issued())


if __name__ == "__main__":
    app.run(debug=True)
