from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from base64 import b64encode
from os import urandom
random_bytes = urandom(10)
token = b64encode(random_bytes).decode('utf-8')
app.secret_key = token

@app.route('/')
def index():
    query = ("SELECT * FROM emails")
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails)

@app.route('/email', methods=['POST'])
def process():
    query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
    data = {
            'email': request.form['email']
    }
    if len(request.form['email']) < 1:
        flash("Email field cannot be empty.")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email adress.")
    else:
        flash("Sucess, email address is {}".format(request.form['email']))
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)

def MySQLConnector(app, db):
    return MySQLConnection(app, db)
