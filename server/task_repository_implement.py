import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.task_repository import TaskRepository
import sqlite3

class TaskRepositoryImplement(TaskRepository):
    
    def __init__(self, db_path = "todolist.db"):
        self.con = sqlite3.connect(f"{db_path}")
        self.con.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.con.cursor()
    
    def insert(self, description):
        self.cur.execute(f"INSERT INTO tasks('description') VALUES ('{description}')")
        self.con.commit()
    
    def delete_one(self, description):
        self.cur.execute(f"DELETE FROM tasks WHERE description='{description}'")
        self.con.commit()
    
    def delete_all(self):
        self.cur.execute("DELETE FROM tasks")
        self.con.commit()
    
    def get_all(self):
        return self.cur.execute("SELECT description FROM tasks").fetchall()