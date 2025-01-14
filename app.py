from flask import Flask, render_template, request
import socket
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB connection URI (
MONGO_URI = os.environ['MONGO_URI']

# MongoDB client connection
client = pymongo.MongoClient(MONGO_URI) 
db = client['admin']

# Define the collection where we will store the request data
collection = db['collection_de_ameliqu']

@app.route("/")
def home():
    name = "Amélie"
    project_name = "minet2.0"
    version = "V2"  
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    client_ip = request.remote_addr
    current_time = datetime.now()

    # Insert into MongoDB
    record = {"ip": client_ip, "date": current_time}
    collection.insert_one(record)

    # Retrieve the last 10 records
    last_records = list(collection.find().sort("_id", -1).limit(10))

    # Generate HTML for the last 10 records
    records_html = "".join(
        f"<li>IP: {record['ip']}, Date: {record['date'].strftime('%Y-%m-%d %H:%M:%S')}</li>"
        for record in last_records
    )

    # Combine everything into an HTML response
    return f"""
    <html>
        <head><title>{project_name}</title></head>
        <body>
            <h1>{project_name} - {version}</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>Date:</strong> {current_date}</p>
            
            <h2>Last 10 Records</h2>
            <ul>
                {records_html}
            </ul>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)