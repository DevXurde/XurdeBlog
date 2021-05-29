from flask import Blueprint, render_template, session, request, redirect
from . import open_settings, db
from .models import Post, Contact
import smtplib

views = Blueprint("views", __name__)

settings = open_settings()


@views.route("/")
def home():
    posts = Post.query.order_by(Post.id)[0:settings["no_of_posts_home"]]
    return render_template("index.html", settings=settings, posts=posts)


@views.route("/posts")
def posts():
    posts = Post.query.order_by(Post.id)
    return render_template("posts.html", settings=settings, posts=posts)


@views.route("/post/<int:id>", methods=["GET", "POST"])
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template("post.html", settings=settings, post=post)


@views.route("/about")
def about():
    return render_template("about.html", settings=settings)


@views.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        body = f"\nName : {name}\nEmail : {email}\nMessage : {message}"

        try:

            add_contact = Contact(name=name, email=email, message=message)
            db.session.add(add_contact)
            db.session.commit()

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("thexurde123@gmail.com", "Earthisround123")
            server.sendmail(
                from_addr="thexurde123@gmail.com",
                to_addrs="zayedmalick13@gmail.com",
                msg=body
            )
            return redirect("/")

        except:
            return "Sorry Email Cannot Be Sent"

    return render_template("contact.html", settings=settings)
