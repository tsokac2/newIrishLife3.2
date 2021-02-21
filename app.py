import os
from flask import (Flask, flash, 
    render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="| Travel | Work | Experience | Life Style")


@app.route("/trip")
def trip():
    return render_template("trip.html", title="| Trip")


@app.route("/work")
def work():
    return render_template("work.html", title="| Work")


@app.route("/life")
def life():
    return render_template("life.html", title="| Life")


@app.route("/tips", methods=["GET", "POST"])
def tips():
    return render_template("tips.html", title="| Tips")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    return render_template('registration.html', title='Register')


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", title="| Login")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template("profile.html", title="| Profile")


@app.route("/logout")
def logout():
    return redirect(url_for("home"))


@app.route("/add_tip", methods=["GET", "POST"])
def add_tip():
    return render_template("add_tip.html", title="| Add Tip")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)