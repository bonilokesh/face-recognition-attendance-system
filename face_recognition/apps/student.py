from flask import Blueprint, session, flash, redirect, url_for, render_template
from utils.attendance import get_attendance

student = Blueprint("student", __name__)

@student.route("/get-attendance", methods = ['GET', 'POST'])
def get_attendance_render():
    if 'current_user' not in session:
        flash("You need to login to access this page", "danger")
        return redirect(url_for("auth.login_user"))
    
    if session['current_user']['role'] != 'STUDENT':
        flash("403 : unauthenticated user")
        return redirect(url_for("auth.login_user"))
    
    a = get_attendance(session['current_user']['email'])
    

    return render_template("get-attendance.html", a = a)

