from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
import sqlite3
app = Flask(__name__)

import os
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from models import *
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    posts = db.session.query(Blog).all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'user' or request.form['password'] != 'pass':
            error = "Invalid credentials. Please try again"
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out')
    return render_template('logout.html')



if __name__ =='__main__':
    app.run(debug=True)
