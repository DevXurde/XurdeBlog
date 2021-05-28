from flask import Blueprint, render_template, session, redirect, request
from . import open_settings
from .login import LoginManager

auth = Blueprint("auth", __name__)

settings = open_settings()
login_manager = LoginManager()


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == settings["admin_user"] and password == settings["admin_password"]:
            login_manager.login(settings["admin_user"])
            return redirect("/dashboard")

    return render_template("login.html", settings=settings, login_manager=login_manager)


@auth.route("/logout")
def logout():
    if login_manager.get_info() == login_manager.logged_in:
        login_manager.logout(settings["admin_user"])
        return redirect("/dashboard")
