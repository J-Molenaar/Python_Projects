from flask import Flask, render_template, request, redirect, session #Add session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' #secret key must be set for security purposes

@app.route('/')
def index():
    return render_template("FormTest/index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # notice how the key we are using to access the info corresponds with the names
    # of the inputs from our html form
    if request.form['action'] == 'login':
        session['email'] = request.form['email']
        return redirect('/sucess')
    elif request.form['action'] == 'register':
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect('/welcome')

@app.route('/sucess')
def sucess():
    return render_template('/FormTest/success.html', email=session['email'])

@app.route('/welcome')
def welcome():
    return render_template('FormTest/welcome.html', name=session['name'], email=session['email'])

app.run(debug=True) # run our server
