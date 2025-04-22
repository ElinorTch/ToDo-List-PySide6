from PySide6 import QtGui
from PySide6.QtWidgets import QApplication
import sys
from adapters.ui.main_ui import MainUI
from core.services.task_services import TaskService
from core.services.category_services import CategoryService
from adapters.storage.sql_task_repository import SqlTaskRepository
from adapters.storage.sql_category_repository import SqlCategoryRepository

if __name__ == "__main__":
    task_repo = SqlTaskRepository()
    task_service = TaskService(task_repo)

    category_rep = SqlCategoryRepository()
    category_service = CategoryService(category_rep)

    app = QApplication([])
    
    font_id = QtGui.QFontDatabase.addApplicationFont("adapters/ui/assets/fonts/Poppins-Regular.ttf")
    font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]

    app.setFont(QtGui.QFont(font_family, 11))

    widget = MainUI(task_service, category_service)
    widget.resize(450, 500)
    widget.show()

    sys.exit(app.exec())