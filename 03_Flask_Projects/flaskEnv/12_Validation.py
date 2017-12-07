from flask import Flask, render_template, redirect, request, session, flash
from base64 import b64encode
from os import urandom
random_bytes = urandom(10)
token = b64encode(random_bytes).decode('utf-8')
app = Flask(__name__)
app.secret_key = token #Genterated via terminal using >>> import os >>>os.urandom(13) () can me any number
print random_bytes
print token
print len(app.secret_key)
@app.route('/')
def index():
        return render_template('validate.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("Name field cannot be empty.") #pass a string into the flash function
    else:
        flash("Sucess, your name is {}".format(request.form['name'])) #pass a string into the flash function
    return redirect('/')

app.run(debug=True)
