import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT,
            lname TEXT,
            email TEXT,
            password TEXT)
                           ''')
        self.connection.commit()

    def insert(self, fname, lname, email, password):
        self.cursor.execute("INSERT INTO users (fname, lname, email, password) VALUES (?, ?, ?, ?)",
                            (fname, lname, email, password))
        self.connection.commit()

    def find_user(self, email, password):
        self.cursor.execute("SELECT fname, lname FROM users WHERE password = ? AND email = ?", (email,password))
        return self.cursor.fetchone()
