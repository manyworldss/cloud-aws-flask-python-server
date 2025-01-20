import os
import logging
PORT = os.getenv('PORT', 5500)  # environment variables 
HOST = os.getenv('HOST', '0.0.0.0')
from flask import Flask, json, jsonify
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/api/item/<id>')
def get_item(id):
     try:
          # looking for an item in database,testing error handling
        if not id.isdigit():
             raise ValueError("ID must be a number")
        return jsonify({"message": f"Found item {id}"})
     
     except ValueError as e:
          return jsonify({"error": str(e)}), 400 # bad request
     

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/contact')
def about():
    return "Contact page"