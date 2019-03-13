from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
import sqlite3
app = Flask(__name__)

import os
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
#app.secret_key = 'm0Lzixs3m0qy'
#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///posts.db'
#database = "posts.db"

#create the sqlalchemy object()
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
'''
    try:
        g.db = connect_db()
        cur = g.db.execute('select * from posts')
        
        for row in cur.fetchall():
            posts.append(dict(no=row[0], title=row[1], description=row[2] ))

        # print(posts)
        #posts =[ dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    
        g.db.close()
    except sqlite3.OperationalError:
        flash("You have no database")

    return render_template('index.html', posts=posts)
'''

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


#def connect_db():
 #xxx   return sqlite3.connect(database)

if __name__ =='__main__':
    app.run(debug=True)
