from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'group3topsecret'
DB_FILE = 'users.db'

def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

@app.route('/')
def home():
    return render_template('landing.html')  # Landing page is your homepage

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password))
            conn.commit()
            conn.close()
            flash('Signup successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already exists. Try logging in.', 'danger')
            return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name, password FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()
        conn.close()

        if result and check_password_hash(result[1], password):
            session['user_name'] = result[0]
            return redirect(url_for('welcome'))
        else:
            flash('Invalid email or password. Try again.', 'danger')
            return redirect(url_for('login'))
    
    # If user visits login page manually, clear session
    session.pop('user_name', None)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home')) 


@app.route('/welcome')
def welcome():
    name = session.get('user_name')
    if not name:
        return redirect(url_for('login'))
    return render_template('welcome.html', name=name)

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/frameworks')
def frameworks():
    return render_template('frameworks.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
