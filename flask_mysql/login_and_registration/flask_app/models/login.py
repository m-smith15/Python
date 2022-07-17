from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash, request
import re
from flask_app import app



# --- MODEL --- 

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

    @classmethod
    def create_user(cls, user_data):

        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        return connectToMySQL('login_and_registration_schema').query_db(query, user_data)
    
    @classmethod
    def validate_login(cls, user_data):

        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('login_and_registration_schema').query_db(query, user_data)

        if len(results) < 1:
            return False

        return cls(results[0])

    @staticmethod
    def validate_registration():
        is_valid = True
        if len(request.form["first_name"]) < 2:
            flash("Name must be at least 2 characters long!")
            is_valid = False
        if len(request.form["last_name"]) < 2:
            flash("Last Name must be at least 2 characters long!")
            is_valid = False
        if not EMAIL_REGEX.match(request.form["email"]):
            flash("Must use a valid email!")
            is_valid = False
        if len(request.form["password"]) < 3:
            flash("pasword less than 3 - replace with bcrypt")
            is_valid = False
        return is_valid

    @staticmethod
    def existing_user_check(email_check):
        is_valid = True

        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('login_and_registration_schema').query_db(query, email_check)

        if results != None:
            is_valid = False

        if request.form["password"] != request.form["password_confirm"]:
            flash("Passwords must match!")
            is_valid = False

        return is_valid
    
