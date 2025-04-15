import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (QListWidget, QListWidgetItem, QApplication, QDialog, QGroupBox,QLabel, QLineEdit, QPushButton, QVBoxLayout)
import sqlite3


class MyWidget(QDialog):

    def __init__(self, task_business_logic):
        super().__init__()

        self.task_service = task_business_logic

        self.setWindowTitle("ToDo-List")
        
        self.edit = QLineEdit("")
        button = QPushButton("Tout supprimer")

        tasks = self.task_service.get_all()
        self.tasks_list = QListWidget()
        for task in tasks:
            self.tasks_list.addItem(f"{task[0]}")
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
        self.task_service.insert(self.edit.text())
        self.tasks_list.addItem(f"{self.edit.text()}")
        self.edit.clear()

    @QtCore.Slot()
    def delete_task(self, item):
        self.tasks_list.takeItem(self.tasks_list.row(item))  
        self.task_service.delete_one(item.text())
        
    @QtCore.Slot()
    def delete_tasks(self):
        self.tasks_list.clear()
        self.task_service.delete_all()