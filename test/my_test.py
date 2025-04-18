import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from logic.task_business_logic import TaskBusinessLogic
from server.task_repository_implement import TaskRepositoryImplement

class TestListeOperations(unittest.TestCase):
    repo = TaskRepositoryImplement()
    task_service = TaskBusinessLogic(repo)

    def test_insert_item(self):
        self.task_service.insert("Description 1")
        tasks_list = self.task_service.get_all_by_category()
        self.assertIn("Description 1", tasks_list[len(tasks_list) - 1])

    def test_delete_item(self):
        self.task_service.delete_one("Description 1")    
        tasks_list = self.task_service.get_all_by_category()
        self.assertNotIn("Description 1", tasks_list[len(tasks_list) - 1])

if __name__ == '__main__':
    unittest.main()
