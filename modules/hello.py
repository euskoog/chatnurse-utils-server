# Import Libraries
from app import app
from flask import jsonify

# Define route "/".


@app.route('/')
def index():
    # return in JSON format. (For API)
    return jsonify({"message": "Welcome to the Chatnurse Utils Server!"})

# Define route "/hello".


@app.route('/hello')
def api():
    # return in JSON format. (For API)
    return jsonify({"message": "Hello from Flask!"})
