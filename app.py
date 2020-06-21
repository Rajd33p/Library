from flask import Flask, render_template, url_for, request, redirect
from features import *

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html", data=B_issued())
    else:
        if request.form['submit'] == "issue":  # issue API
            issue(request.form['Fname'],  # Name
                  # Int converted addmission number
                  int(request.form['addno']),
                  int(request.form['BookID']))  # Int converted Book ID

        if request.form['submit'] == "collect":  # Collect API
            collect(int(request.form['I_ID']))

        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
