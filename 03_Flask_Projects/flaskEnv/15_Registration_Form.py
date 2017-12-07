from flask import Flask, render_template, request, redirect, flash
import re # the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from base64 import b64encode
from os import urandom
random_bytes = urandom(10)
token = b64encode(random_bytes).decode('utf-8')
app = Flask(__name__)
app.secret_key = token #Genterated via terminal using >>> import os >>>os.urandom(13) () can me any number

@app.route('/')
def form():
   return render_template("/RegistrationForm/Form.html")
   print "Got Post Info"

@app.route('/registration', methods=['POST'])
def create_user():
    print "Got Post Info"
    first = request.form['first']
    last = request.form['last']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']
    if len(request.form['email']) < 1:
        flash("Email field cannot be empty.") #pass a string into the flash function
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email adress.")
    else:
        flash("Sucess, email address is {}".format(request.form['email'])) #pass a string into the flash function
    if len(request.form['first']) < 1:
        flash("Name field cannot be empty.") #pass a string into the flash function, check len()
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comments cannot be more than 120 characters.") #pass a string into the flash function, check len()
        return redirect('/')
    else:
        return redirect('/success')

@app.route('/sucess')
        return render_template('/RegistrationForm/success.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True) # run our server
