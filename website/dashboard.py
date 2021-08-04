from flask import Blueprint, render_template, session, request, redirect
from . import open_settings, db
from .models import Post

dashboard = Blueprint("dashboard", __name__)

settings = open_settings()


@dashboard.route("/dashboard")
def dashboard_func():
    if "admin" in session and session["admin"] == settings["admin_user"]:
        posts = Post.query.order_by(Post.id)
        return render_template("dashboard.html", settings=settings, posts=posts)

    else:
        return redirect("/login")


@dashboard.route("/add_post", methods=["GET", "POST"])
def add_post():
    if "admin" in session and session["admin"] == settings["admin_user"]:

        if request.method == "POST":
            title = request.form.get("title")
            tagline = request.form.get("tagline")
            author = request.form.get("author")

            content = request.form.get("content")

            new_post = Post(title=title, tagline=tagline,
                            author=author, html=content)
            db.session.add(new_post)
            db.session.commit()

            return redirect("/dashboard")

        return render_template("add_post.html", settings=settings)

    else:
        return redirect("/dashboard")


@dashboard.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "admin" in session and session["admin"] == settings["admin_user"]:

        if request.method == "POST":
            title = request.form.get("title")
            tagline = request.form.get("tagline")
            author = request.form.get("author")

            content = request.form.get("content")

            new_post = Post.query.filter_by(id=id).update(dict(
                title=title,
                tagline=tagline,
                author=author,
                html=content
            ))
            db.session.commit()

            return redirect("/dashboard")

        post = Post.query.filter_by(id=id).first()
        return render_template("edit.html", settings=settings, post=post)

    else:
        return redirect("/dashboard")


@dashboard.route("/delete/<int:id>")
def delete(id):
    if "admin" in session and session["admin"] == settings["admin_user"]:

        post = Post.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()

        return redirect("/dashboard")

    else:
        return redirect("/dashboard")
