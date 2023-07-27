from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secretkeyforblogapp"

    #this import is the variable views defined inside views.py
    from .views import views
    from .auth import auth

    #url_prefix can be used to define something we would want in the url before our pages name
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
