from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route('/signin')
def signin(): 
    return render_template("signin.html")

@auth.route('/signup')
def signup(): 
    return render_template("signup.html")

@auth.route('/signout')
def signout(): 
    #referencing the function name not the route or endpoint
    return redirect(url_for("views.home"))
