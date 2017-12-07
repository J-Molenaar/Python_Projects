from flask import Flask, render_template #import the Flask module and import the render_template module so the html will display

app = Flask(__name__) #create an "app" variable which represents our web application.

@app.route('/') #set up a routing rule using the "@" symbol and running the app.route function.

def test1():
    print 'in index method'
    return render_template('test1.html')

@app.route('/test2') #set up a routing rule using the "@" symbol and running the app.route function.

def test2():
    print 'in index method'
    return render_template('test2.html')

app.run(debug = True)


#once done, in VE, run 'python server.py' to activate server so you can see the live html
