from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = ('SELECT * FROM friends')
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html', all_friends=friends) #pass the data to the index.html!

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>') #where <friend_id> = any id on list
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id} #Important! We are using the format :variable_name to inject values into a query string. This is a way of asking SQL Alchemy to parse the values being inserted into our string in order to protect against any suspicious looking data. Hackers use something known as SQL injection to attack sites. Imagine if a hacker typed "DELETE FROM users WHERE id > 0" into one of your input fields.
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    return render_template('index.html', all_friends=friends) #still pass it what the html shows

@app.route('/update')
def update():
    query = ('SELECT * FROM friends')
    friends = mysql.query_db(query)
    return render_template('update.html', all_friends=friends)

@app.route('/update_friend', methods=['POST'])
def updatefriend():
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': request.form['id']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': request.form['id']}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
