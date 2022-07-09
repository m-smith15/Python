from flask import Flask, render_template, session, request, redirect #remember session needs secret key

app = Flask(__name__)
app.secret_key = "example secret key"

@app.route("/")
def landing_page():
    print("landing page")
    if "countPy" not in session:
        session["countPy"] = 0
    if "visits" not in session:
        session["visits"] = 1
    else:
        session["visits"] += 1
    return render_template("index.html")

@app.route("/click")
def clicked_button():
    print("button clicked")
    session["countPy"] += 1
    return redirect("/")

@app.route("/click/2/")
def clicked_button_two():
    print("button x2 clicked")
    session["countPy"] += 2
    return redirect("/")

@app.route("/click/form", methods=["POST"])
def clicked_send():
    print("int button clicked")
    session["countPy"] += int(request.form["click_input"])
    return redirect("/")

@app.route("/destroy_session")
def reset_clicked():
    print("reset request sent")
    session["countPy"] = 0
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)