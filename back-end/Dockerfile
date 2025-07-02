# משתמשים בתמונה רשמית של פייתון 3.11 בגרסה קטנה
FROM python:3.11-slim

# מגדירים את תיקיית העבודה בקונטיינר
WORKDIR /app

# מעתיקים את כל הקבצים לתוך תיקיית העבודה
COPY . .

# מתקינים את התלויות מתוך requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# פותחים פורט 5000, זה הפורט ש־Flask מאזין אליו
EXPOSE 5000

# מריצים את היישום
CMD ["python", "app.py"]