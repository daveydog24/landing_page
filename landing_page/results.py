from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/dojos/new')
def dojos():
  return render_template("dojo.html")

@app.route('/dojos/new', methods=['POST'])
def dojo():
  print "Got dojos info"
  name = request.form['name']
  email = request.form['email']
  return render_template("dojo.html", got_name = name, got_email = email)
  return redirect('/dojos/new')

app.run(debug=True)