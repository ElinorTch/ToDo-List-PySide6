import sys
import random
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox,QLabel, QLineEdit, QPushButton, QVBoxLayout)


class MyWidget(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDo-List")
        self.create_tasks_group_box()
        
        self.edit = QLineEdit("")
        button = QPushButton("Tout supprimer")
        button.setAutoDefault(False)

        button.clicked.connect(self.delete_tasks)
        self.edit.returnPressed.connect(self.add_task)

        main_layout = QVBoxLayout(self)

        main_layout.addWidget(self._tasks_group_box)
        main_layout.addWidget(self.edit)
        main_layout.addWidget(button)

    
    def create_tasks_group_box(self):
        self._tasks_group_box = QGroupBox("Liste des taches")
        self.tasks_layout = QVBoxLayout()
        self.tasks_layout.setAlignment(QtCore.Qt.AlignTop)
        self._tasks_group_box.setLayout(self.tasks_layout)

    @QtCore.Slot()
    def add_task(self):
        text = QLabel(f"{self.edit.text()}")
        self.tasks_layout.addWidget(text)
        self.edit.clear()
    
    @QtCore.Slot()
    def delete_tasks(self):
        while self.tasks_layout.count():
            item = self.tasks_layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.setParent(None)


if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(250, 300)
    widget.show()

    sys.exit(app.exec())