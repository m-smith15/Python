from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.users import Users

# CONTROLLER

@app.route('/')
def index():
    users = Users.get_all()
    print(users)
    return render_template("Read_all.html", all_users = users)
#updating this from the friends.py file. This is reaching out the models > users file to pull data from the DB and then render the read_all page in templates

# relevant code snippet from server.py
@app.route('/create', methods=["POST"])
def create_user():
    #data will be dictionary we use, and we'll populate it from from on webpage
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # now we send data variable to MODEL > USER to insert into DB
    Users.save(data)
    # send us back to the readall landing page to see our update
    return redirect('/')

#handling for routing to create user page
@app.route('/create_user')
def create_user_page():
    return render_template('create.html')

#handling for routing to delete user
@app.route('/delete_user/<int:usernum>')
def delete_user(usernum):
    data = {
        "id": usernum
    }
    Users.delete(data)
    return redirect('/')

#show 1 user
@app.route('/show/<int:usernum>')
def show_user(usernum):
    data = {
        "id": usernum
    }
    single_user = Users.show_one(data)
    return render_template("Read_one.html", user = single_user)

#Edit user query
@app.route('/edit_user/<int:usernum>', methods=["POST"])
def edit_user(usernum):
    data = {
        "id": usernum,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Users.edit(data)
    return redirect('/')

#Edit user landing page 
@app.route('/edit/<int:usernum>')
def edit_page(usernum):
    data = {
        "id": usernum
    }
    single_user = Users.show_one(data)
    return render_template("edit.html", user = single_user)


