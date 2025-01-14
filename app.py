from flask import Flask, render_template
import socket
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB connection URI (
MONGO_URI = os.environ['MONGO_URI']

# MongoDB client connection
client = pymongo.MongoClient(MONGO_URI + 'admin') # mets le nom de la db que tu veux (précisable dans le yaml du docker compose)
db = client.get_default_database()

# Define the collection where we will store the request data
collection = db.requests

@app.route("/")
def home():
    name = "Amélie"
    project_name = "minet2.0"
    version = "V1"
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Return a simple HTML response or use a template
    return f"""
    <html>
        <head><title>{project_name}</title></head>
        <body>
            <h1>{project_name} - {version}</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>Date:</strong> {current_date}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)