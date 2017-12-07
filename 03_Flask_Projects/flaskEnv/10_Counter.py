from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'fff'

@app.route('/')
def index():
    if not "count" in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('/Counter/Count.html')

@app.route('/dothing', methods=['post'])
def dothing():
    if request.form['f'] == '1':
        session['count'] += 1
    elif request.form['f'] == '2':
        session['count'] -= session['count']
    return redirect('/')

app.run(debug=True)
