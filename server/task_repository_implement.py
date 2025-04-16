from logic.task_repository import Task_repository
import sqlite3

class Task_repository_implement(Task_repository):
    
    def __init__(self, db_path = "todolist.db"):
        self.con = sqlite3.connect(f"{db_path}")
        self.cur = self.con.cursor()
    
    def insert(self, description):
        self.cur.execute(f"INSERT INTO task('description') VALUES ('{description}')")
        self.con.commit()
    
    def delete_one(self, description):
        self.cur.execute(f"DELETE FROM task WHERE description='{description}'")
        self.con.commit()
    
    def delete_all(self):
        self.cur.execute("DELETE FROM task")
        self.con.commit()
    
    def get_all(self):
        return self.cur.execute("SELECT description FROM task").fetchall()