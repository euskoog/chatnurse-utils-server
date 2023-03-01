# Import Libraries
from app import app
from flask import jsonify

# Define route "/hello".


@app.route('/hello')
def api():
    # return in JSON format. (For API)
    return jsonify({"message": "Hello from Flask!"})
