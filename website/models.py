from . import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(1000))
    tagline = db.Column(db.String(1000))
    author = db.Column(db.String(1000))

    html = db.Column(db.Text)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())
