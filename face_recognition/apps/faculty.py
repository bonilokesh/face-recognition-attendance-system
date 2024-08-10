from flask import Blueprint, session, flash, redirect, url_for, request, render_template
from utils.attendance import mark_attendence
from utils.query import get_result

faculty = Blueprint("faculty", __name__)

@faculty.route("/mark-attendance", methods = ['GET', 'POST'])
def add_attendance_render():
    if 'current_user' not in session:
        flash("You need to login to access this page", "danger")
        return redirect(url_for("auth.login_user"))
    
    if session['current_user']['role'] != 'FACULTY':
        flash("403 : unauthenticated user")
        return redirect(url_for("auth.login_user"))
    
    if request.method == "POST":
        course_name = request.form.get("course_name")
        slot = request.form.get("slot")
        file = request.files.get("image")
        file_path = "temp.png"
        file.save(file_path)

        res = get_result(file_path)
        mark_attendence(course_name, slot, res, 1)

        return render_template("faculty/attendence-result.html")

    return render_template("mark-attendance.html")

