from abc import ABC, abstractmethod


class TaskPort(ABC):
    @abstractmethod
    def insert(self, description, label): pass
    
    @abstractmethod
    def delete_one(self, description): pass
    
    @abstractmethod
    def delete_all(self): pass
    
    @abstractmethod
    def get_all_by_category(self, categorie_label): pass
    
    @abstractmethod
    def update(self, id, new_description): pass
    
    @abstractmethod
    def get_completion_pourcentage(self, label): pass

    @abstractmethod
    def get_one(self, description): pass

    @abstractmethod
    def checked(self, is_checked, description): pass