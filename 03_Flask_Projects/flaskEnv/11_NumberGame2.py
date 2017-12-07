from flask import Flask, render_template, request, redirect, session, flash
from random import randint
app = Flask(__name__)
app.secret_key = 'shhh'

@app.route('/')
def index():
    if not 'random' in session:
        session['random'] = randint(1,101)
    print session['random']
    return render_template('/NumbersGame/numbergame.html')

@app.route('/dothing', methods=['post'])
def dothing():
    guess = int(request.form['guess'])
    if guess > session['random']:
        flash('Too high, guess again.')
    elif guess < session['random']:
        flash('Too low, guess again.')
    else:
        flash('You win!!')
    print session['guess']
    return redirect('/')

@app.route('/r')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
