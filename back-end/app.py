from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import os
import json
from google.oauth2 import id_token
from google.auth.transport import requests as grequests

app = Flask(__name__)
CORS(app)

dancers = [
    {"id": 1, "name": "Daniel", "level": "Intermediate"},
    {"id": 2, "name": "Maya", "level": "Beginner"},
    {"id": 3, "name": "Raz", "level": "Pro"},
    {"id": 4, "name": "Brian", "level": "Master"},
]

@app.route('/api/dancers', methods=['GET'])
def get_dancers():
    return jsonify(dancers)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    token = data.get('token')

    try:
        # שים פה את ה־CLIENT_ID שלך שקיבלת מ־Google Cloud Console
        CLIENT_ID = "707475720698-omp6m2gnpm6huagif3gck0t78rm1roq6.apps.googleusercontent.com"
        idinfo = id_token.verify_oauth2_token(token, grequests.Request(), CLIENT_ID)

        # אימות תקין, חילוץ מידע משתמש
        user_id = idinfo['sub']
        user_email = idinfo['email']
        user_name = idinfo.get('name')

        # בניית תגובה עם קידוד עברית תקין
        response_data = {
            "message": f"Welcome {user_name}!",
            "email": user_email,
            "user_id": user_id
        }

        return Response(
            json.dumps(response_data, ensure_ascii=False),
            content_type='application/json; charset=utf-8'
        )

    except ValueError:
        # הטוקן אינו תקין
        return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
