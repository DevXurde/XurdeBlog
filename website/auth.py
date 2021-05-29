from flask import Blueprint, render_template, session, redirect, request
from . import open_settings

auth = Blueprint("auth", __name__)

settings = open_settings()


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == settings["admin_user"] and password == settings["admin_password"]:
            session["admin"] = settings["admin_user"]
            return redirect("/dashboard")

    return render_template("login.html", settings=settings)


@auth.route("/logout")
def logout():
    if "admin" in session and session["admin"] == settings["admin_user"]:
        session.pop("admin")
        return redirect("/dashboard")
