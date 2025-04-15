class Task_business_logic():

    def __init__(self, task_repository):
        self.repo = task_repository

    def insert(self, description):
        self.repo.insert(description)

    def delete_one(self, description):
        self.repo.delete_one(description)

    def delete_all(self):
        self.repo.delete_all()

    def get_all(self):
        return self.repo.get_all()
