from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cakes')
def cakes():
	return 'Yummy Cakes!'

@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)
	#<name> plaatst de input als variable, en wordt opgepakt door de functie hello
	

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

#0.0.0.0 betekent dat ieder device op het netwerk erbij kan
# als deze app.py gerund wordt met python3, dan kun je via 127.0.0.1:5000 de pagina bekijken
# hostname -I zoekt ip-adres op van huidige netwerk, dan poort 5000 van dat ip-adres laat website zien


# https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/



# https://github.com/easink/aioheos/tree/master/aioheos
