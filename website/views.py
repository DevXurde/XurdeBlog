from flask import Blueprint, render_template, session, request, redirect
from . import open_settings, db
from .models import Post
from .login import LoginManager

views = Blueprint("views", __name__)

settings = open_settings()
login_manager = LoginManager()


@views.route("/")
def home():
    posts = Post.query.order_by(Post.id)[0:3]
    return render_template("index.html", settings=settings, posts=posts, login_manager=login_manager)


@views.route("/posts")
def posts():
    posts = Post.query.order_by(Post.id)
    return render_template("posts.html", settings=settings, posts=posts, login_manager=login_manager)


@views.route("/post/<int:id>", methods=["GET", "POST"])
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template("post.html", settings=settings, post=post, login_manager=login_manager)


@views.route("/about")
def about():
    return render_template("about.html", settings=settings, login_manager=login_manager)


@views.route("/contact")
def contact():
    return render_template("contact.html", settings=settings, login_manager=login_manager)
