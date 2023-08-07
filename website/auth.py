from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route('/signin')
def signin(): 
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('User Signed In!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("signin.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method == 'POST':
        #accessing the name parameter in the html forms inside the get method and assigning it to a variable with the same name
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # ERROR CHECKING AT SIGNUP
        #using .first() becuase this will grab the first instance found of that email and all emails should be unique
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash('This email is already associated with an account.', category='error')
        elif username_exists:
            flash('This username is already in use.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4: 
            flash('Email is invalid.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created successfully!')
            return redirect(url_for('views.home'))

    return render_template("signup.html")

@auth.route('/signout')
@login_required
def signout(): 
    logout_user()
    #referencing the function name not the route or endpoint
    return redirect(url_for("views.home"))
