from flask import Flask, render_template #improting Flask module
# import render
app = Flask(__name__) #creating a new instance of Flask called variable app

@app.route('/') #the landing page of the route. The URL doesn't need to have the / in it (ex localhost:5000)
def hello_world():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/dojo')
def hello_dojo():
    return "Hello Dojo!"

@app.route('/say/<string:name>')
def hello_input(name):
    name = name.capitalize()
    return f"Hello {name}!!"

@app.route('/repeat/<int:x>/<string:repeat>')
def repeat_input(x, repeat):
    #type of x int
    #return render of html file
    return f"{repeat} {x} times <br> \n" * x

@app.errorhandler(404)
def page_not_found(error):
    return f"That page doesn't exist! 404"
    # checking if route is valid, if not redirect to a 404 method that says not found


if __name__ == "__main__": #this ensures file is being run directly and not diff module. Sets app to run in debug mode
    app.run(debug=True)
