from flask import Flask, render_template, redirect, request, session, flash
import re # the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # create a regular expression object that we can use run operations on
from base64 import b64encode
from os import urandom
random_bytes = urandom(10)
token = b64encode(random_bytes).decode('utf-8')
app = Flask(__name__)
app.secret_key = token #Genterated via terminal using >>> import os >>>os.urandom(13) () can be any number

@app.route('/')
def index():
        return render_template('validate_email.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
        flash("Email field cannot be empty.") #pass a string into the flash function
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email adress.")
    else:
        flash("Sucess, email address is {}".format(request.form['email'])) #pass a string into the flash function
    return redirect('/')

app.run(debug=True)
