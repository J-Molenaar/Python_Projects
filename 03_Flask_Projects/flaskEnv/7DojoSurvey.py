from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def form():
   return render_template("/DojoSurvey/Form.html")
   print "Got Post Info"

@app.route('/name', methods=['POST'])
def create_user():
   print "Got Post Info"
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   print name
   return render_template('/DojoSurvey/success.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True) # run our server
