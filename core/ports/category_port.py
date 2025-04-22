from abc import ABC, abstractmethod


class CategoryPort(ABC):
    @abstractmethod
    def insert(self, label) -> None: pass

    @abstractmethod
    def delete_one(self, label): pass
    
    @abstractmethod
    def delete_all(self): pass

    @abstractmethod
    def get_all(self): pass

