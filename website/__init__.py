from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secretkeyforblogapp"
    #telling flask where the db is
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #initializing db
    db.init_app(app)

    #this import is the variable views defined inside views.py
    from .views import views
    from .auth import auth

    #url_prefix can be used to define something we would want in the url before our pages name
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    #import models before db is created so the tables get created properly
    from.models import User

    create_database(app)

    login_manager = LoginManager()
    #redirects user to sign in if not already logged in
    login_manager.login_view = "auth.signin"
    login_manager.init_app(app)

    @login_manager.user_loader
    #function looks at User model, queries it, and get the id that is equal to the id passed in
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        #not best practice but fine for local production
        print("Created database")