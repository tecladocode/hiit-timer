from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "jose"


@app.route("/", methods=["GET", "POST"])
def setup():
    if request.method == "POST":
        exercise = int(request.form["exercise"])
        rest = int(request.form["rest"])
        sets = int(request.form["sets"])

        session["exercise"] = exercise
        session["rest"] = rest
        session["sets"] = sets
        session["set_counter"] = 0

        return redirect(url_for("rest"))
    return render_template("home.jinja2")


@app.route("/rest")
def rest():
    return render_template("rest.jinja2", rest=session["rest"])


@app.route("/exercise")
def exercise():
    if session["set_counter"] == session["sets"]:
        return redirect(url_for("completed"))
    session["set_counter"] += 1
    return render_template("exercise.jinja2", exercise=session["exercise"])


@app.route("/complete")
def completed():
    return render_template("complete.jinja2", sets=session["set_counter"])
