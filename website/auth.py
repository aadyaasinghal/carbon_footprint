from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash
# function adds a new row to the existing data the two inputs are df1 and df2 output is y
def add_row(df1, df2):
    y = pd.concat([df1, df2])
    return y
# tells flask to add a authorization pg
auth = Blueprint("auth", __name__)
@auth.route("/", methods = ["GET","POST"])
def login():
    if request.method == "POST": 
        email = request.form.get("email")
        password = request.form.get("password")
        login_info = pd.read_csv("login_info.csv",index_col="email")
        emails = login_info.index
        if email in emails and login_info.loc[email,"password"] == password:
            flash("Signed In Successfully", category = "success")
            session["current_user"] = email
            #return render_template(url_for("views.home"))
            return render_template("home.html")

        elif email in emails and not login_info.loc[email,"password"]==password:
            flash("Passowrd Incorrect", category = "error")
        else:
            flash("Email is not registered", category = "error")
    return render_template("login.html")


@auth.route("/sign-up", methods = ["GET","POST"])
def signup():

    if request.method == "POST": 
        email = request.form.get("email")
        name = request.form.get("name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        duplicate_data = pd.read_csv("login_info.csv")
        list_data = list(duplicate_data)

        if password1 != password2:
            flash("Passwords do not match", category="error")
        elif email in list_data:
            flash("Account already created", category = "error")
        else:
            duplicate_data = pd.read_csv("login_info.csv",index_col="email")
            new_user = {"email":[email], "name":[name], "password":[password1]}
            new_user1 = pd.DataFrame(new_user)
            new_user1.set_index("email", inplace=True)
            new_loginInfo = add_row(duplicate_data, new_user1)
            new_loginInfo.to_csv("login_info.csv")
            return redirect(url_for("auth.login"))
    return render_template("sign_up.html")