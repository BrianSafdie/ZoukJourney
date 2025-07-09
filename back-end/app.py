from flask_cors import CORS
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

dancers = [
    {"id": 1, "name": "Daniel", "level": "Intermediate"},
    {"id": 2, "name": "Maya", "level": "Beginner"}
]

@app.route('/api/dancers', methods=['GET'])
def get_dancers():
    return jsonify(dancers)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    # Validate token here...
    return jsonify({"message": "Login successful!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)