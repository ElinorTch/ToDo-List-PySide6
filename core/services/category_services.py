import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ports.category_port import CategoryPort

class CategoryService():
    def __init__(self, repository: CategoryPort):
        self.repo = repository
    
    def insert(self, label):
        self.repo.insert(label)

    def delete_one(self, label):
        self.repo.delete_one(label)

    def delete_all(self):
        self.repo.delete_all()

    def get_all(self):
        return self.repo.get_all()
    
    def get_one(self, label):
        return self.repo.get_one(label)