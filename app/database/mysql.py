# app/database/mysql.py
import mysql.connector
from app.models.user import UserCreate, User

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="fuser"
        )
        self.cursor = self.db.cursor()

    def create_user(self, user: UserCreate) -> int:
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (user.username, user.email, user.password)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.lastrowid

    def get_user(self, user_id: int) -> User:
        query = "SELECT id, username, email, password FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        user_data = self.cursor.fetchone()
        if user_data:
            return User(id=user_data[0], username=user_data[1], email=user_data[2], password=user_data[3])
        return None

    def update_user(self, user_id: int, user: UserCreate) -> bool:
        query = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s"
        values = (user.username, user.email, user.password, user_id)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.rowcount > 0

    def delete_user(self, user_id: int) -> bool:
        query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.db.commit()
        return self.cursor.rowcount > 0
