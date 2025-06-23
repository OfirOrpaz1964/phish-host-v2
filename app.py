from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST', 'GET'])
def log_data():
    ip = request.remote_addr
    data = request.get_data(as_text=True)
    now = datetime.utcnow().isoformat()

    with open("log.txt", "a") as f:
        f.write(f"[{now}] {ip} → {data}\n")

    return "Logged", 200

@app.route('/')
def index():
    return "Logger is up."
