from flask import Flask, render_template
import socket
from datetime import datetime

app = Flask(__name__)

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