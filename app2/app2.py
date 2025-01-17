from flask import Flask, render_template, request
import socket
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    name = "Amélie"
    project_name = "minet2.0"
    version = "V2"  
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    client_ip = request.remote_addr
    current_time = datetime.now()

    return f"""
    <html>
        <head><title>{project_name}</title></head>
        <body>
            <h1>{project_name} - {version}</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>Date:</strong> {current_date}</p>
            
            <h2>Page numero2 sans DB</h2>

        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)