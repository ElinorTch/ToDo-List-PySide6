import sys
import random
from PySide6 import QtCore
from PySide6.QtWidgets import (QListWidget, QListWidgetItem, QApplication, QDialog, QGroupBox,QLabel, QLineEdit, QPushButton, QVBoxLayout)


class MyWidget(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDo-List")
        # self.create_tasks_group_box()
        
        self.edit = QLineEdit("")
        button = QPushButton("Tout supprimer")
        self.tasks_list = QListWidget()
        self.tasks_list.itemDoubleClicked.connect(self.delete_task)

        button.setAutoDefault(False)

        button.clicked.connect(self.delete_tasks)
        self.edit.returnPressed.connect(self.add_task)

        main_layout = QVBoxLayout(self)

        main_layout.addWidget(self.tasks_list)
        main_layout.addWidget(self.edit)
        main_layout.addWidget(button)

    @QtCore.Slot()
    def add_task(self):
        self.tasks_list.addItem(f"{self.edit.text()}")
        self.edit.clear()

    def delete_task(self, item):
        self.tasks_list.takeItem(self.tasks_list.row(item))  
        
    @QtCore.Slot()
    def delete_tasks(self):
        self.tasks_list.clear()


if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(250, 300)
    widget.show()

    sys.exit(app.exec())