import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (QListWidget, QListWidgetItem, QApplication, QDialog, QGroupBox,QLabel, QLineEdit, QPushButton, QVBoxLayout)
import sqlite3


con = sqlite3.connect("todolist.db")
cur = con.cursor()
tasks = cur.execute("SELECT description FROM task").fetchall()

class MyWidget(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDo-List")
        
        self.edit = QLineEdit("")
        button = QPushButton("Tout supprimer")

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
        cur.execute(f"INSERT INTO task('description') VALUES ('{self.edit.text()}')")
        con.commit()
        self.tasks_list.addItem(f"{self.edit.text()}")
        self.edit.clear()

    def delete_task(self, item):
        self.tasks_list.takeItem(self.tasks_list.row(item))  
        cur.execute(f"DELETE FROM task WHERE description='{item.text()}'")
        con.commit()
        
    @QtCore.Slot()
    def delete_tasks(self):
        self.tasks_list.clear()
        cur.execute("DELETE FROM task;")
        con.commit()


if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(250, 300)
    widget.show()

    sys.exit(app.exec())