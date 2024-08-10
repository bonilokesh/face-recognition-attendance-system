import re
from flask import Blueprint, flash, request, render_template, session, redirect, url_for
from utils.admin import login

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login_user():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        result = login(email, password)

        if not result:
            flash("Invalid user details", "danger")
            return render_template("login.html")
        
        else:
            session['current_user'] = result
            
            return redirect(url_for("home.home_render"))


    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.pop("current_user", None)
    return redirect(url_for("auth.login_user"))
