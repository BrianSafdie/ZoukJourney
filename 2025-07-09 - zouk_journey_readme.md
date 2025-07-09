# Zouk Journey Project

This project is a simple full-stack web application built to manage and display a list of Zouk dancers. It consists of a front-end written in HTML/CSS/JavaScript and a back-end API built using Python's Flask framework. The full system is containerized with Docker and can be deployed to the cloud (e.g., Render).

---

## 🗂 Project Structure

```
zouk-journey/
├── front-end/
│   ├── index.html
│   ├── about.html
│   └── style.css
│
├── back-end/
│   ├── app.py
│   ├── requirements.txt
│   └── env/ (virtual environment - ignored in Git)
│
└── .git/
```

---

## 🚀 Features

- View a list of Zouk dancers (GET request)
- Add new dancers (POST request)
- Navigate between pages (index / about)
- Styled front-end and connected Flask back-end
- Front-end and back-end both deployable to Render

---

## 🧪 Local Development

### 📦 Prerequisites

- Python 3.11+
- Node.js Live Server extension for VS Code (for local front-end)
- Docker (for optional containerized back-end)

### ✅ Run Locally (Without Docker)

```bash
# Back-end
cd back-end
python -m venv env
./env/Scripts/activate
pip install -r requirements.txt
py app.py

# Front-end
# Open front-end/index.html with Live Server in VS Code
```

---

### 🐳 Docker Version

```bash
cd back-end
# Build Docker image
docker build -t zouk-back-end .

# Run container on port 5050
docker run -d -p 5050:5000 zouk-back-end

# Backend now available at:
http://127.0.0.1:5050/api/dancers
```

---

## ☁️ Deployment to Render

### 🔷 Front-End

1. Create a new **Static Site** in Render.
2. Set the root directory to `front-end/`.
3. Deploy from your GitHub repo.

### 🔷 Back-End

1. Create a new **Web Service** in Render.
2. Set the root directory to `back-end/`.
3. Ensure `requirements.txt` contains:
   ```
   flask
   flask-cors
   ```
4. The entry point is `app.py`
5. Flask app must be configured to run on `host='0.0.0.0'`

### 🧩 CORS

Make sure your `app.py` has CORS enabled:

```python
from flask_cors import CORS
CORS(app)
```

---

## 🔗 Connecting Front and Back

Update JavaScript in `index.html` to call the API:

```js
fetch('https://<your-backend-service>.onrender.com/api/dancers')
```

---

## 📝 Todo

-

---

## 👨‍💻 Author

Created by Brian Safdie.

