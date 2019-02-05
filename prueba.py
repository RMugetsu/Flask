from flask import Flask, request, session
import random
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def hello():
    if 'random' in session:
        rand = session['random']
        print(rand)
    else:
        rand = int(random.randrange(1,100,1))
        session['random'] = rand
    return """<form action='login' method='POST'>
    	<label>Adivina el numero</label>
    	<input type=number name=num></input>
    	<input type=submit>
    </form>
    """


@app.route('/login',methods = ['POST'])
def login():
  if request.method == "POST":
    num = int(request.form['num'])
    if num < session['random']:
    	return "El numero introducido es mas pequeño "
    if num > session['random']:
    	return "El numero introducido es mas grande"
    if num == session['random']:
    	return "El numero introducido es correcto"
  else:
   	return "No funciona"