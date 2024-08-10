from flask import Flask
from apps.student import student
from apps.faculty import faculty
from apps.admin import admin
from apps.home import home
from apps.auth import auth

app = Flask(__name__)
app.secret_key = "this-is-secret"

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(faculty)
app.register_blueprint(student)

if __name__ == "__main__":
    app.run(debug=True)
