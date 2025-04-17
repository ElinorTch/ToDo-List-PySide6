from PySide6 import QtCore
from PySide6.QtWidgets import (QMenu, QApplication, QTreeWidgetItem, QTreeWidget, QComboBox, QListWidget, QInputDialog, QDialog, QLineEdit, QPushButton, QVBoxLayout)
from PySide6.QtGui import QCursor, QAction

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
                child = QTreeWidgetItem([task[1]])
                item.addChild(child)
                child.setFlags(child.flags() | QtCore.Qt.ItemIsUserCheckable)
                if task[3] == True:
                    child.setCheckState(0, QtCore.Qt.Checked)
                else:
                    child.setCheckState(0, QtCore.Qt.Unchecked)
                self.tree.itemDoubleClicked.connect(self.delete_task)
            items.append(item)

        self.tree.insertTopLevelItems(0, items)
        self.tree.itemPressed.connect(self.handle_item_pressed)
        self.tree.itemChanged.connect(self.on_item_checked)
        
        self.edit = QLineEdit("")
        self.edit.returnPressed.connect(self.add_task)
        button = QPushButton("Tout supprimer")
        button.setAutoDefault(False)
        button.clicked.connect(self.delete_tasks)
        
        self.category_button_dialog = QPushButton("Ajouter une categorie")
        self.category_button_dialog.clicked.connect(self.add_category)
        self.category_button_dialog.setAutoDefault(False)

        self.category_choice = QComboBox()
        for categorie in categories:
            self.category_choice.addItems(categorie) 

        main_layout = QVBoxLayout(self)

        main_layout.addWidget(self.tree)
        main_layout.addWidget(self.edit)
        main_layout.addWidget(self.category_choice)
        main_layout.addWidget(self.category_button_dialog)
        main_layout.addWidget(button)


    @QtCore.Slot()
    def on_item_checked(self, item, column):
        if item.checkState(column) == QtCore.Qt.Checked:
            self.task_service.checked(True, item.text(column))
        else:
            self.task_service.checked(False, item.text(column))

    @QtCore.Slot()
    def handle_item_pressed(self, item, column):
        mouse_buttons = QApplication.mouseButtons()
        if mouse_buttons == QtCore.Qt.RightButton:
            pos = QCursor.pos()
            menu = QMenu()
            modifier = QAction("Modifier", self)
            modifier.triggered.connect(lambda: self.modify_Category(item.text(0)))
            menu.addAction(modifier)
            menu.exec_(pos)
    
    @QtCore.Slot()
    def modify_Category(self, item):
        print(item)
        pass

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
        child = QTreeWidgetItem([self.edit.text()])
        item[0].addChild(child)
        child.setFlags(child.flags() | QtCore.Qt.ItemIsUserCheckable)
        child.setCheckState(0, QtCore.Qt.Unchecked)
        self.edit.clear()

    @QtCore.Slot()
    def delete_task(self, item):
        self.task_service.delete_one(item.text(0))
        if item.parent():
            item.parent().removeChild(item)
        
    @QtCore.Slot()
    def delete_tasks(self):
        self.task_service.delete_all()