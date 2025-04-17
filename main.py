from PySide6.QtWidgets import QApplication
from view.task_user_side import MyWidget
import sys
from server.task_repository_implement import TaskRepositoryImplement
from logic.task_business_logic import TaskBusinessLogic
from logic.category_business_logic import CategoryBusinessLogic
from server.category_repository_implement import CategoryRepositoryImplement

if __name__ == "__main__":
    repo = TaskRepositoryImplement()
    task_service = TaskBusinessLogic(repo)

    category_rep = CategoryRepositoryImplement()
    category_service = CategoryBusinessLogic(category_rep)

    app = QApplication([])

    widget = MyWidget(task_service, category_service)
    widget.resize(250, 300)
    widget.show()

    sys.exit(app.exec())