import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(""" 
         CREATE TABLE IF NOT EXISTS users (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         user_id VARCHAR(20),
         username VARCHAR(20),
         phone_number VARCHAR(50)
         );
         """)
        self.conn.commit()

    def add_users(self, user_id, username, phone_number):
        self.cursor.execute("INSERT INTO users (user_id, username, phone_number) VALUES (?, ?, ?);", (user_id, username, phone_number))
        self.conn.commit()

    def check_user(self, user_id):
        user = self.cursor.execute("SELECT * FROM users WHERE user_id = ?;", (user_id,)).fetchone()
        return user