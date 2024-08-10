from flask import Blueprint, session, flash, redirect, url_for, render_template

home = Blueprint("home", __name__)

@home.route("/")
def home_render():
    if 'current_user' not in session:
        flash("You need to login to access this page", "danger")
        return redirect(url_for("auth.login_user"))

    if session['current_user']['role'] == 'FACULTY':
        return redirect(url_for("faculty.add_attendance_render"))
    
    if session['current_user']['role'] == 'STUDENT':
        return redirect(url_for("student.get_attendance_render"))
    
    return render_template("dashboard.html")
    
    
