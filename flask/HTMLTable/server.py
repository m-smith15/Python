from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users_infoPy = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users = users_infoPy)


@app.errorhandler(404)
def page_not_found(error):
    return f"That page doesn't exist! 404"

if __name__ == "__main__":
    app.run(debug=True)