import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.ports.category_port import CategoryPort
import sqlite3

class SqlCategoryRepository(CategoryPort):
    def __init__(self, db_path = "todolist.db"):
        self.con = sqlite3.connect(f"{db_path}")
        self.con.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.con.cursor()

    def insert(self, label):
        self.cur.execute(f"INSERT INTO categories(label) VALUES ('{label}')")
        self.con.commit()
    
    def delete_one(self, label):
        self.cur.execute(f"DELETE FROM categories WHERE label='{label}'")
        self.con.commit()
    
    def delete_all(self):
        self.cur.execute("DELETE FROM categories")
        self.con.commit()
    
    def get_all(self):
        return self.cur.execute("SELECT label FROM categories").fetchall()