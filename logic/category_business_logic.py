class CategoryBusinessLogic():
    def __init__(self, category_repository_implement):
        self.repo = category_repository_implement
    
    def insert(self, label):
        self.repo.insert(label)

    def delete_one(self, label):
        self.repo.delete_one(label)

    def delete_all(self):
        self.repo.delete_all()

    def get_all(self):
        return self.repo.get_all()