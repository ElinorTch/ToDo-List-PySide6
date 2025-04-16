import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from logic.task_business_logic import Task_business_logic
from server.task_repository_implement import Task_repository_implement

class TestListeOperations(unittest.TestCase):
    repo = Task_repository_implement()
    task_service = Task_business_logic(repo)

    def test_insert_item(self):
        self.task_service.insert("Description 1")
        tasks_list = self.task_service.get_all()
        self.assertIn("Description 1", tasks_list[len(tasks_list) - 1])

    def test_delete_item(self):
        self.task_service.delete_one("Description 1")    
        tasks_list = self.task_service.get_all()
        self.assertNotIn("Description 1", tasks_list[len(tasks_list) - 1])

if __name__ == '__main__':
    unittest.main()
