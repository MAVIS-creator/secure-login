# Secure Login System with Salted Password Hashing

## 📌 Overview
This project is a **Python-based secure login system** that uses **salted password hashing** to protect user credentials.  
It stores hashed passwords in an SQLite database (`users.db`) instead of saving plain-text passwords.

---

## ✨ Features
- Secure password storage using **PBKDF2_HMAC** hashing
- Random **salt** generation for each password
- SQLite database for persistent user data
- User registration and login verification
- Prevention against rainbow table attacks
- Command-line interface for testing

---

## 🛠 Requirements
- Python **3.8+**
- SQLite (comes pre-installed with Python)
- `hashlib` (built-in)
- `sqlite3` (built-in)

---

## 📥 Installation
1. **Clone or Download** the project
    git clone https://github.com/MAVIS-creator/secure-login.git


2. **Open in Code Editor**
    - Launch your **Code Editor**
    - Open the project folder

3. **Install the requirements needed**
    - Open terminal in your environment 
    - Run pip install -r requirements.txt

4. **Run the project in terminal**
    python app.py
    
5. - Run the given address there

---

## 🔑 How Salted Password Hashing Works
- When a user registers:
  1. A **unique salt** is generated for that user.
  2. The password is hashed with the salt using **PBKDF2_HMAC**.
  3. The salt and hash are stored in the database.

- When a user logs in:
  1. The stored salt is retrieved.
  2. The entered password is hashed with the same salt.
  3. If the hash matches, access is granted.

This method prevents hackers from using pre-computed hash tables to crack passwords.

---

## 📂 Database Structure (`users.db`)
The database contains a `users` table with:
| id  | username | salt | password_hash |
|-----|----------|------|---------------|

---

## 🔍 How to View Salted Passwords in `users.db`
1. Open a terminal and run:
    ```bash
    sqlite3 users.db
    ```
2. Show all users:
    ```sql
    SELECT * FROM users;
    ```
3. You will see:
    - **username**: The account name  
    - **salt**: The random salt in hex format  
    - **password_hash**: The hashed password in hex format  

---

## ⚠ Security Notes
- **Never store plain-text passwords**
- Use a **strong hashing algorithm** with sufficient iterations
- Keep salts unique and random for each user
- Regularly update dependencies and security practices

---

## 📜 License
This project is for **educational purposes** and should be adapted for production environments with extra security measures.
