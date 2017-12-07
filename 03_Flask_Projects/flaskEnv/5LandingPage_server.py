from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')

def home():
    print 'in index method'
    return render_template('LandingPage/Home.html')

@app.route('/ninja')

def ninja():
    print 'in index method'
    return render_template('LandingPage/Ninja.html')

@app.route('/form')

def form():
    print "Got Post Info"
    # return render_template('LandingPage/Form.html')
    return render_template('LandingPage/Form.html')

app.run(debug = True)
