from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    #db columns that hold user information
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    #default will fill this by default with whatever the current time is
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())