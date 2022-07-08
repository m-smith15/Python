from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:xPy>/<int:yPy>/<string:color1Py>/<string:color2Py>')
def render_checkerboard(xPy,yPy,color1Py,color2Py):

    return render_template("index.html", x = xPy, y = yPy, color1 = color1Py, color2 = color2Py)

@app.route('/<int:xPy>')
def render_checkerboard_xinput(xPy):
    yPy = 8
    color1Py = 'red'
    color2Py = 'black'
    return render_template("index.html", x = xPy, y = yPy, color1 = color1Py, color2 = color2Py)

@app.route('/')
def render_checkerboard_default():
    xPy = 8
    yPy = 8
    color1Py = 'red'
    color2Py = 'black'
    return render_template("index.html", x = xPy, y = yPy, color1 = color1Py, color2 = color2Py)


@app.errorhandler(404)
def page_not_found(error):
    return f"That page doesn't exist! 404"

if __name__ == "__main__":
    app.run(debug=True)
