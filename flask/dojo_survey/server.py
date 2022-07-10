from flask import Flask, session, redirect, request, render_template

app = Flask(__name__)
app.secret_key = "shrimpaholic"

@app.route("/")
def landing_page():
    print("Landing Page reached")
    
    session['form_results'] = []

    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results_page():
    print("Results page reached!")

    new_form_results = {
        "name": request.form["name"],
        "location": request.form["location"],
        "comments": request.form["comments"],
        "radio_button": request.form["radio_button"],
        "checkbox_yes": request.form["checkbox_yes"],
        "checkbox_no": request.form["checkbox_no"]
    }
    session["form_results"].append(new_form_results)
    session.modified = True
    print(session["form_results"])
    return render_template("results.html")

@app.route("/destroy_session")
def reset_clicked():
    print("reset request sent")
    session["form_results"] = []
    session.modified = True
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)