__author__ = 'hanyuen'

from flask import Flask, render_template,\
    request,redirect, url_for, session, flash, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from database import db

from models import Train



app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db.init_app(app)


def create_admin():
    admin = Admin(app, name="TrainsBooking")
    admin.add_view(ModelView(Train, db.session))


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("you need to log in first")
            return redirect((url_for("login")))
    return wrap


@app.route("/")
@login_required
def home():
    trains = db.session.query(Train).all()
    return render_template("index.html", trains = trains)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form["user"] != 'admin' or request.form["password"] != 'admin'):
            error = "Invalid credentials. Please try again"
        else:
            session["logged_in"] = True
            flash("you were just logged in")
            return redirect(url_for('home'))

    return render_template("login.html", error = error)

@app.route("/logout")
@login_required
def logout():
    session.pop('logged_in', None)
    flash("you were just logged out")
    return redirect (url_for("welcome"))


if __name__ == '__main__':
    create_admin()
    app.run()