from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')

def hello_world():
    print 'in index method'
    return render_template('HelloWorld/HelloWorld.html')

app.run(debug = True)
