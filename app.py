from flask import Flask, render_template, url_for, request, redirect, flash
from features import *


app = Flask(__name__)
app.secret_key = "sjdnfgisudngjisegiosno"


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html", data=B_issued())
    else:
        if request.form['submit'] == "issue":  # issue API
            issue_res(request.form)

        if request.form['submit'] == "collect":
            collect_res(request.form['I_ID'])

        return redirect(url_for("home"))


def issue_res(data):
    try:
        ID = issue(data['fname'], int(data['addno']), int(data['BookID']))
        flash('You Issue ID is ' + str(ID), 'alert-success')
    except:
        flash('An Exception occurred', 'alert-warning')


def collect_res(ID):
    try:
        res = collect(int(ID))
        if(res.isdigit()):
            flash('Please Collect fine of ' + str(res), 'alert-success')
        elif res == "ID_NOT_FOUND":
            flash('ID not Found', 'alert-danger')
        else:
            flash('Please Collect the Book', 'alert-success')
    except:
        flash('An Exception occurred', 'alert-warning')


if __name__ == "__main__":
    app.run(debug=True)
