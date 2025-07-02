from flask import Flask, jsonify

app = Flask(__name__)

dancers = [
    {"id": 1, "name": "Daniel", "level": "Intermediate"},
    {"id": 2, "name": "Maya", "level": "Beginner"}
]

@app.route('/api/dancers', methods=['GET'])
def get_dancers():
    return jsonify(dancers)

if __name__ == '__main__':
    app.run(debug=True, port=5000)