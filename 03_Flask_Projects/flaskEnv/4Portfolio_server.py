from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')

def home():
    print 'in index method'
    return render_template('Portfolio/Home.html')

@app.route('/about')

def about():
    print 'in index method'
    return render_template('Portfolio/About.html')

@app.route('/projects')

def projects():
    print 'in index method'
    return render_template('Portfolio/Projects.html')

app.run(debug = True)
