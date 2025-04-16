from PySide6.QtWidgets import QApplication
from view.task_user_side import MyWidget
import sys
from server.task_repository_implement import Task_repository_implement
from logic.task_business_logic import Task_business_logic

if __name__ == "__main__":
    repo = Task_repository_implement()
    task_service = Task_business_logic(repo)

    tasks = task_service.get_all()

    app = QApplication([])

    widget = MyWidget(task_service)
    widget.resize(250, 300)
    widget.show()

    sys.exit(app.exec())