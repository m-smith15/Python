from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.login import User

# --- CONTROLLER ---  

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def login_page():
    if session.get("is_logged_in") is not None:
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@app.route("/register", methods=["POST"])
def register():
    
    #look to see if they already exist in the DB or not
    email_check = {
        "email": request.form["email"]
    }

    if not User.existing_user_check(email_check):
        print("user exists")
        flash("That email is already in use")
        return redirect('/')
    else:
        print("user does not exist in DB")

    #validation of the request form
    if not User.validate_registration():
        print("form entries are NOT valid")
        return redirect('/')
    else:
        print("form entries are valid")

    #pw hashing and dropping into DB
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    User.create_user(user_data)

    #once in DB add to session cookie
    session['is_logged_in'] = True
    session['email'] = user_data["email"]

    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    
    user_data = {
        "email": request.form["email"]
    }
    user_exists = User.validate_login(user_data)

    if not user_exists:
        flash("invalid email")
        return redirect("/")

    if not bcrypt.check_password_hash(user_exists.password, request.form["password"]):
        flash("invalid Password")
        return redirect('/')

    session['is_logged_in'] = True
    session['email'] = user_data["email"]

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    #session['is_logged_in'] = False
    session.pop('email', None)
    session.pop('is_logged_in', None)
    
    return redirect('/')
