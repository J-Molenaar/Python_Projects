from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def form():
   return render_template("/WhatsMyName/Form.html")
   print "Got Post Info"

@app.route('/name', methods=['POST'])
def create_user():
   print "Got Post Info"
   name = request.form['name']
   print name
   return render_template('/WhatsMyName/success.html', name = name)

app.run(debug=True) # run our server
