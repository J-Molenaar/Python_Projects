from flask import Flask, render_template, request, redirect, session, flash
from random import randint
app = Flask(__name__)
app.secret_key = 'fff'

@app.route('/')
def index():
    try:
        if session['won']:
            pass
    except:
        session['won'] = 0
        session['lost'] = 0
        session['tie'] = 0
    return render_template('RockPaper.html')

@app.route('/dothing', methods=['post'])
def dothing():
    list =['Rock', 'Paper', 'Scissors']
    randNum = str(randint(0,2))
    if request.form['f'] == '0' and randNum == '2':
        flash('You win!')
        session['won'] += 1
    elif request.form['f'] == '1' and randNum == '0':
        flash('You win!')
        session['won'] += 1
    elif request.form['f'] == '2' and randNum == '1':
        flash('You win!')
        session['won'] += 1
    elif request.form['f'] == randNum:
        flash ('Its a tie')
        session['tie'] += 1
    else:
        flash('It is a Tie')
        session['lost'] += 1
    flash('You played {}'.format(list[int(request.form['f'])]))
    return redirect('/')

app.run(debug=True)
