from flask import Flask, render_template #import the Flask module and import the render_template module so the html will display

app = Flask(__name__) #create an "app" variable which represents our web application.

@app.route('/')

def tmnt():
    print 'in index method'
    return render_template('TurtleNinjas/tmnt.html')

@app.route('/<color>')
def color(color):
    if color == 'red':
        return render_template('TurtleNinjas/red.html')
    elif color == 'blue':
        return render_template('TurtleNinjas/blue.html')
    elif color == 'purple':
        return render_template('TurtleNinjas/purple.html')
    elif color == 'orange':
        return render_template('TurtleNinjas/ornage.html')
    else:
        return render_template('TurtleNinjas/notapril.html')

app.run(debug = True)
