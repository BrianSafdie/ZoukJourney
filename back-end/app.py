from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dancers = [
    {"id": 1, "name": "Daniel", "level": "Intermediate"},
    {"id": 2, "name": "Maya", "level": "Beginner"}
]

@app.route('/api/dancers', methods=['GET'])
def get_dancers():
    return jsonify(dancers)

if __name__ == '__main__':
    app.run(debug=True, port=5000)