from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from os import urandom
import binascii
import re
import md5
app = Flask(__name__)
app.secret_key = 'fff'
mysql = MySQLConnector(app,'myuserdb')

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/wall')
    return render_template('index.html')

@app.route('/signup')
def signup():
    if 'user' in session:
        return redirect('/wall')
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def submitEmail():
    name_regex = re.compile(r'\d')
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors = 0

    if request.form['first_name'] == '' or request.form['last_name'] == '' or request.form['email'] == '' or request.form['pass1'] == '':
        flash("All fields must be filled in.")
        return redirect('/signup')
    if name_regex.search(request.form['first_name']) or name_regex.search(request.form['last_name']):
        notEnoughChars = ''
        if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
            notEnoughChars = ' and must be at least 2 letters long'
        flash("Your name cannot have any numbers in it{}.".format(notEnoughChars))
        errors += 1
    if not email_regex.match(request.form['email']):
        flash("That is NOT a valid email... come on...")
        errors += 1
    if request.form['pass1'] == '':
        flash("You're gonna need a password to register...")
        errors += 1
    if request.form['pass1'] != request.form['pass2']:
        flash("Typed passwords don't match.")
        errors += 1
    if len(request.form['pass1']) < 8:
        flash("Password must be at least 8 characters")
        errors += 1
    
    if errors == 0:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['pass1']
        salt = binascii.b2a_hex(urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()

        query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw,
            'salt': salt
        }
        mysql.querydb(query, data)
        session['email'] = email
        flash("Registration Successful!")
        return redirect('/wall')
    else:
        return redirect('/signup')
        

@app.route('/login', methods=['POST'])
def login():
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    if len(request.form['email']) == 0 or not email_regex.match(request.form['email']):
        flash("Please enter a valid email address.")
        return redirect('/')
    elif len(request.form['pass']) == 0:
        flash("Please enter your password.")
        return redirect('/')
    else:
        email = request.form['email']
        password = request.form['pass']
        userQuery = "SELECT * FROM users WHERE email = :email LIMIT 1"
        queryData = {
            'email': email
        }
        user = mysql.querydb(userQuery, queryData)
        session['user'] = user
        if len(user) !=0:
            encrypted_pw = md5.new(password + user[0]['salt']).hexdigest()
            if encrypted_pw == user[0]['password']:
                session['email'] = email
                return redirect('/wall')
            else:
                flash("Password invalid.")
                return redirect('/')
        else:
            flash("Email not linked to registered account.")
            return redirect('/')

@app.route('/wall')
def account():
    if session['email']:
        userQuery = "SELECT id, first_name, last_name FROM users WHERE email = :email LIMIT 1"
        queryData = {
            'email': session['email']
        }
        session['user'] = mysql.querydb(userQuery, queryData)

        postsQuery = "SELECT messages.message, users.id AS user_id, messages.id, messages.active, CONCAT(users.first_name, ' ', users.last_name) AS name, DATE_FORMAT(messages.created_at, '%M %D, %Y - %h:%m%p') AS created_at FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
        # postsData = {
        #     'user_id': session['user'][0]['id']
        # }
        session['messages'] = mysql.querydb(postsQuery)

        commentsQuery = "SELECT comments.comment, comments.message_id, CONCAT(users.first_name, ' ', users.last_name) AS name, comments.created_at FROM comments JOIN users ON comments.user_id = users.id JOIN messages ON comments.message_id = messages.id"
        session['comments'] = mysql.querydb(commentsQuery)

        print session['comments']
        return render_template('account.html')
    else:
        flash("Please login.")
        return redirect('/')

@app.route('/postMsg', methods=['POST'])
def postMsg():
    postQuery = "INSERT INTO messages (user_id, message, active, created_at, updated_at) VALUES (:user_id, :message, 1, NOW(), NOW())"
    postData = {
        'user_id': session['user'][0]['id'],
        'message': request.form['msg']
    }
    mysql.querydb(postQuery, postData)

    return redirect('/wall')
    
@app.route('/postComment', methods=['POST'])
def postComment():
    postQuery = "INSERT INTO comments (user_id, comment, created_at, updated_at, message_id) VALUES (:user_id, :comment, NOW(), NOW(), :message_id)"
    postData = {
        'user_id': session['user'][0]['id'],
        'message_id': request.form['msg_id'],
        'comment': request.form['comment']
    }
    mysql.querydb(postQuery, postData)
    return redirect('/wall')

@app.route('/deletePost/<msg_id>')
def deletePost(msg_id):
    deleteQuery = "UPDATE messages SET active = 0 WHERE messages.id = :message_id"
    deleteData = {
        'message_id': msg_id
    }
    mysql.querydb(deleteQuery, deleteData)
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)