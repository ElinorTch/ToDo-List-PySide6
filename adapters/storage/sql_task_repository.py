import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.ports.task_port import TaskPort
import sqlite3

class SqlTaskRepository(TaskPort):
    
    def __init__(self, db_path = "todolist.db"):
        self.con = sqlite3.connect(f"{db_path}")
        self.con.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.con.cursor()
    
    def insert(self, description, label):
        self.cur.execute(f"INSERT INTO tasks('description', 'categorie_label') VALUES ('{description}', '{label}')")
        self.con.commit()
    
    def delete_one(self, description):
        self.cur.execute(f"DELETE FROM tasks WHERE description='{description}'")
        self.con.commit()
    
    def delete_all(self):
        self.cur.execute("DELETE FROM tasks")
        self.con.commit()
    
    def get_all_by_category(self, categorie_label):
        return self.cur.execute(f"SELECT * FROM tasks WHERE categorie_label = '{categorie_label}'").fetchall()

    def get_one(self, description):
        return self.cur.execute(f"SELECT * FROM tasks WHERE description = '{description}'").fetchone()

    def checked(self, checked, description):
        self.cur.execute(f"UPDATE tasks SET done = {checked} WHERE description = '{description}'")
        self.con.commit()

    def update(self, description, new_description):
        self.cur.execute(f"UPDATE tasks SET description = '{new_description}', updated_at = CURRENT_TIMESTAMP WHERE description = '{description}'")
        self.con.commit()

    def get_completion_pourcentage(self, label):
        return self.cur.execute(f"SELECT COUNT(*) FROM tasks WHERE done = 1 and categorie_label = '{label}'").fetchall()
