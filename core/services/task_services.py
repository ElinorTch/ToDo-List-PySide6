import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ports.task_port import TaskPort

class TaskService():
    def __init__(self, repository: TaskPort):
        self.repo = repository

    def insert(self, description, label):
        self.repo.insert(description, label)

    def delete_one(self, description):
        self.repo.delete_one(description)

    def delete_all(self):
        self.repo.delete_all()

    def get_all_by_category(self, categorie_label):
        return self.repo.get_all_by_category(categorie_label)

    def checked(self, is_checked, description):
        return self.repo.checked(is_checked, description)
    
    def update(self, description, new_description):
        return self.repo.update(description, new_description)
    
    def get_completion_pourcentage(self, label):
        return self.repo.get_completion_pourcentage(label)
    
    def get_one(self, description):
        return self.repo.get_one(description)
