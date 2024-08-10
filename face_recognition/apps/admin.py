from flask import Blueprint, session, flash, redirect, url_for, request, render_template
from utils.admin import add_faculty, add_student
from utils.insert import insert

admin = Blueprint("admin", __name__)

@admin.route("/add-faculty", methods = ['GET', 'POST'])
def add_faculty_render():
    if 'current_user' not in session:
        flash("You need to login to access this page", "danger")
        return redirect(url_for("auth.login_user"))
    
    if session['current_user']['role'] != 'ADMIN':
        flash("403 : unauthenticated user")
        return redirect(url_for("auth.login_user"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        result = add_faculty(name, email, password)

        if result:
            flash("Faculty added successfully", "success")
        
        else:
            flash("Email already register", "danger")

        return redirect(url_for("admin.add_faculty_render"))

    return render_template("admin/add-faculty.html")

@admin.route("/add-student", methods = ['GET', 'POST'])
def add_student_render():
    if 'current_user' not in session:
        flash("You need to login to access this page", "danger")
        return redirect(url_for("auth.login_user"))
    
    if session['current_user']['role'] != 'ADMIN':
        flash("403 : unauthenticated user")
        return redirect(url_for("auth.login_user"))
    
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        file = request.files.get("image")
        file_path = "temp.png"

        result = add_student(name, email, password)

        if result:
            file.save(file_path)
            insert(file_path, email)
            flash("Student added successfully", "success")
        
        else:
            flash("Email already register", "danger")

        return redirect(url_for("admin.add_student_render"))

    return render_template("admin/add-student.html")

