from PySide6 import QtCore
from PySide6.QtWidgets import (QTreeWidgetItem, QTreeWidget, QComboBox, QListWidget, QInputDialog, QDialog, QLineEdit, QPushButton, QVBoxLayout)


class MyWidget(QDialog):

    def __init__(self, task_business_logic, category_business_logic):
        super().__init__()

        self.task_service = task_business_logic
        self.category_service = category_business_logic

        self.setWindowTitle("ToDo-List")

        categories = self.category_service.get_all()

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Arbre des taches"])
        items = []
        for category in categories:
            item = QTreeWidgetItem([category[0]])
            tasks = self.task_service.get_all(category[0])
            for task in tasks:
                child = QTreeWidgetItem([task[0]])
                item.addChild(child)
            items.append(item)

        self.tree.insertTopLevelItems(0, items)
        
        self.edit = QLineEdit("")
        self.edit.returnPressed.connect(self.add_task)
        button = QPushButton("Tout supprimer")
        button.setAutoDefault(False)
        button.clicked.connect(self.delete_tasks)
        
        self.category_button_dialog = QPushButton("Ajouter une categorie")
        self.category_button_dialog.clicked.connect(self.add_category)
        self.category_button_dialog.setAutoDefault(False)


        self.tasks_list = QListWidget()
        for task in tasks:
            self.tasks_list.addItem(f"{task[0]}")
        self.tasks_list.itemDoubleClicked.connect(self.delete_task)

        self.category_choice = QComboBox()
        for categorie in categories:
            self.category_choice.addItems(categorie) 

        main_layout = QVBoxLayout(self)

        main_layout.addWidget(self.tree)
        # main_layout.addWidget(self.tasks_list)
        main_layout.addWidget(self.edit)
        main_layout.addWidget(self.category_choice)
        main_layout.addWidget(self.category_button_dialog)
        main_layout.addWidget(button)

    @QtCore.Slot()
    def add_category(self):
        text, ok = QInputDialog.getText(
            self,
            "New Category",
            "Enter category name:"
        )
        if ok and text:
            self.category_service.insert(text)
            self.tree.addTopLevelItem(QTreeWidgetItem([text]))
            self.category_choice.addItem(text) 

    @QtCore.Slot()
    def add_task(self):
        self.task_service.insert(self.edit.text(), self.category_choice.currentText())
        item = self.tree.findItems(self.category_choice.currentText(), QtCore.Qt.MatchExactly, 0)
        item[0].addChild(QTreeWidgetItem([self.edit.text()]))
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