from flask import Flask, session, redirect, request, render_template
import random

app = Flask(__name__)
app.secret_key = "shrimpaholic"

@app.route("/")
def landing_page():
    print("Landing page reached")

    if "guess_number" not in session:
        session["guess_number"] = random.randint(1,100)

    if "guess" not in session:
        session["guess"] = 0
        print("guess was reset")
    if "guess_hist" not in session:
        session["guess_hist"] = []
        print("guess history reset")


    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess_sent():

    new_guessed_number = {
        "guess": request.form["guess"]
    }

    print(session["guess_hist"])
    session["guess_hist"].append(new_guessed_number)

    session["guess"] = int(request.form["guess"])
    print(session["guess"])
    print(session["guess_number"])

    session.modified = True
    
    return redirect("/")

@app.route("/play_again", methods=["POST"])
def retry_game():
    session["guess"] = 0
    session["guess_hist"] = []

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)