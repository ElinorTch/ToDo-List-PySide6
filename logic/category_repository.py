from abc import ABC, abstractmethod


class CategoryRepository(ABC):
    @abstractmethod
    def insert(self, label) -> None: pass

    @abstractmethod
    def delete_one(self, label): pass
    
    @abstractmethod
    def delete_all(self): pass

    @abstractmethod
    def getAll(self): pass
    
    @abstractmethod
    def getOne(self, label): pass