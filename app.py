from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mani@3005',
    database='flask_web_db'
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])  
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Received: Name={name}, Email={email}, Password={password}")
    if not name or not email or not password:
        return 'Invalid data received'

    try:
        query = "INSERT INTO user_data (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, password)
        cursor.execute(query, values)
        db.commit()
        return 'Data Saved Successfully'
    except Exception as e:
        return f"Database Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
