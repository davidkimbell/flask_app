from flask import Flask, render_template, request # http://flask.pocoo.org
import os
from weather import get_weather

app = Flask(__name__)

# app.run(debug=True) #To avoid restarting your Flask app after every code change (REMOVE FOR PRODUCTION!!!)

@app.route("/")
def index():
	# name = request.values.get('name')
	# return render_template('index.html', name=name)
	address = request.values.get('address')
	forecast = None
	if address:
		forecast = get_weather(address)
	return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
