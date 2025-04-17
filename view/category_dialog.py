from PySide6.QtWidgets import (QApplication, QColorDialog, QCheckBox, QDialog,
                               QErrorMessage, QFontDialog, QFileDialog, QFrame,
                               QGridLayout, QGroupBox, QInputDialog, QLabel,
                               QLineEdit, QMessageBox, QPushButton,
                               QSizePolicy, QSpacerItem, QToolBox,
                               QVBoxLayout, QWidget)


class CategoryDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        