from flask import Flask, request, make_response
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/log', methods=['POST', 'GET'])
def log_data():
    ip = request.remote_addr
    data = request.get_data(as_text=True)
    now = datetime.utcnow().isoformat()
    log_line = f"[{now}] {ip} → {data}"

    # Log to stdout so Render can show it
    print(log_line, flush=True)

    response = make_response("Logged", 200)
    response.mimetype = "text/plain"
    return response

@app.route('/')
def index():
    return "Logger is up."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env var
    app.run(host='0.0.0.0', port=port)
