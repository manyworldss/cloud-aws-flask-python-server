from flask import Flask, json, jsonify
import os
import boto3
import logging

PORT = os.getenv('PORT', 5500)  # environment variables 
HOST = os.getenv('HOST', '0.0.0.0')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/aws-test')
def test_aws():
    try:
        # Create an S3 client, # Try to connect to AWS S3
        s3 = boto3.client('s3')
        
        # Try to list buckets (simple test) , # Ask AWS "show me what buckets I can access"
        response = s3.list_buckets()
        
        return jsonify({
            "message": "AWS Connection Successful",
            "buckets": [bucket['Name'] for bucket in response['Buckets']]
        })
    except Exception as e:
        return jsonify({"error": f"AWS Connection Failed: {str(e)}"}), 500

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


@app.route('/create-bucket')
def create_bucket():
    try:
        # Connect to S3
        s3 = boto3.client('s3')
        
        # Name for  new bucket
        bucket_name = "max-movies-score-data-99"

        # Create the bucket with location constraints
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration={
                             'Location Constraint': 'us east 1' 
                         })
        return jsonify({"message": f"Bucket {bucket_name} created successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# tells python to run the flask server in debug mode 

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
