from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninja import Ninja

# --------- CONTROLLER PAGE --------------

#dojos will need 3 app routes and methods. One to show all dojos on landing page, one to show individual dojo when selected, one to add a new dojo to the list

@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos = dojos)

@app.route('/create_new_dojo', methods=['POST'])
def create_new_dojo():
    data = {
        "name": request.form["new_dojo"]
    }
    Dojo.add_dojo(data)
    return redirect('/')

@app.route('/dojos/<int:dojonum>')
def show_one_dojo(dojonum):
    data = {
        "id": dojonum
    }
    dojos = Dojo.show_one_dojo(data)
    return render_template("dojo_details.html", dojo = dojos)

@app.route('/ninjas')
def add_ninja():

    dojos = Dojo.get_all_dojos()

    return render_template("ninjas.html", all_dojos = dojos)

@app.route('/ninjas/add', methods=['POST'])
def add_ninja_submit():
    data = {
        "first_name":request.form["first_name"],
        "last_name": request.form["last_name"],
        "age" :request.form["age"],
        "dojo_id" : request.form["dojo_location"]
    }

    Ninja.add_ninja(data)
    return redirect('/')
