from datetime import timedelta

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

from features import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '0TO1BUgdT5HpRt2OjvvS'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)


admins = {
    "username":["admin","Rajdeep"],
    "password":["admin","Saha"]
}

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        if "user" in session:
            return redirect(url_for("home"))
        else:
            return render_template("login.html")
    if request.method == "POST":
       session.permanent = True
       name =  request.form["username"]  
       passw =  request.form["password"]  
       
       if ((name in admins["username"]) and (passw in admins["password"])):
           session["user"] = name
           return redirect(url_for("home"))
       else:
            return render_template("login.html")
            
 
@app.route("/home", methods=["POST", "GET"])
def home():
    if "user" in session:
        if request.method == "GET":
            return render_template("home.html", data=B_issued(), book=BookS())
        else:
            if request.form['submit'] == "issue":  # issue API
                issue_res(request.form)

            if request.form['submit'] == "collect":
                collect_res(request.form['I_ID'])

            return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))



def issue_res(data):
    try:
        ID = issue(data['Fname'], int(data['addno']), int(data['BookID']))
        flash('You Issue ID is ' + str(ID), 'alert-success')
    except:
        flash('An Exception occurred', 'alert-warning')
   


def collect_res(ID):
    
    try:
        res = str(collect(int(ID)))
        if(res.isdigit()):
            flash('Please Collect fine of ' + str(res), 'alert-success')
        elif res == "ID_NOT_FOUND":
            flash('ID not Found', 'alert-danger')
        else:
            flash('Please Collect the Book', 'alert-success')
    except:
        flash('An Exception occurred', 'alert-warning')
    



if __name__ == "__main__":
    app.run(threaded=True, port=5000)
