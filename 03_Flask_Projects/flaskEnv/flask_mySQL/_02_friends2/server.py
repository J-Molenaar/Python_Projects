from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = ("SELECT name, age, DATE_FORMAT(friend_since, '%M %d, %Y') AS friend_since FROM friends")
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends) #pass the data to the index.html!

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (name, age, friend_since) VALUES (:name, :age, NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
def MySQLConnector(app, db):
    return MySQLConnection(app, db)
