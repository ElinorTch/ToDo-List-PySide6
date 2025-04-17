class TaskBusinessLogic():

    def __init__(self, task_repository):
        self.repo = task_repository

    def insert(self, description, label):
        self.repo.insert(description, label)

    def delete_one(self, description):
        self.repo.delete_one(description)

    def delete_all(self):
        self.repo.delete_all()

    def get_all(self, categorie_label):
        return self.repo.get_all(categorie_label)

    def checked(self, is_checked, description):
        return self.repo.checked(is_checked, description)
    
    def update(self, description, new_description):
        return self.repo.update(description, new_description)
