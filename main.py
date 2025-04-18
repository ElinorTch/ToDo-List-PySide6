from PySide6 import QtGui
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
    
    font_id = QtGui.QFontDatabase.addApplicationFont("view/assets/fonts/Poppins-Regular.ttf")
    font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]

    app.setFont(QtGui.QFont(font_family, 11))

    widget = MyWidget(task_service, category_service)
    widget.resize(450, 500)
    widget.show()

    sys.exit(app.exec())