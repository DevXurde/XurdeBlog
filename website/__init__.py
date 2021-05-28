from flask import Flask
import json
import os
from flask_sqlalchemy import SQLAlchemy


def open_settings():
    with open("settings.json", "r") as file:
        args = json.load(file)
    return args


db = SQLAlchemy()
settings = open_settings()

DB_NAME = settings["db_name"]

host = settings["host"]
port = settings["port"]


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings["secret_key"]
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SERVER_NAME"] = f"{host}:{port}"

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .dashboard import dashboard

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(dashboard, url_prefix="/")

    from .models import Post
    create_database(app)

    return app


def create_database(app):
    if not os.path.exists("website"+DB_NAME):
        db.create_all(app=app)
