from flask import Flask, request, make_response
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST', 'GET'])
def log_data():
    ip = request.remote_addr
    data = request.get_data(as_text=True)
    now = datetime.utcnow().isoformat()
    log_line = f"[{now}] {ip} → {data}"

    print(log_line, flush=True)

    # Explicit clean HTTP response
    response = make_response("Logged", 200)
    response.mimetype = "text/plain"
    return response

@app.route('/')
def index():
    return "Logger is up."
