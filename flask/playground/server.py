from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:numPy>/<colorPy>')
def number_and_color_page(numPy,colorPy):
    if(colorPy == ""):
        colorPy = "Skyblue"
    return render_template("index.html",num=numPy,color=colorPy)

@app.route('/play/<int:numPy>') #number but no color
def number_page(numPy):
    colorPy = "Skyblue"
    return render_template("index.html",num=numPy,color=colorPy)

@app.route('/play') #default, no number or color
def default_page():
    numPy = 3
    colorPy = 'Skyblue'
    return render_template("index.html",num=numPy,color=colorPy)


@app.errorhandler(404)
def page_not_found(error):
    return f"That page doesn't exist! 404"

if __name__ == "__main__":
    app.run(debug=True)