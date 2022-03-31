from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QLineEdit, QListWidget, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout, QGridLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste de tâches")
        self.setWindowIcon(QtGui.QIcon('res/icon.png'))
        self.setMinimumSize(400, 400)
        self.setStyleSheet("background-color:rgba(40, 40, 40, 0.72);")

        main_layout = QVBoxLayout(self)

        self.list = QListWidget()
        self.list.setStyleSheet("color: cyan;")
        self.task_adding = QLineEdit()
        self.task_adding.setStyleSheet("background-color:white;")
        self.btn_clear = QPushButton("Tout supprimer")
        self.btn_clear.setStyleSheet("background-color:white;")

        self.task_adding.setPlaceholderText("Ajouter une nouvelle tâche...")

        main_layout.addWidget(self.list)
        main_layout.addWidget(self.task_adding)
        main_layout.addWidget(self.btn_clear)

        self.btn_clear.clicked.connect(self.list.clear)
        self.task_adding.returnPressed.connect(self.insert_task)
        self.list.itemDoubleClicked.connect(self.remove_task)

    def insert_task(self):
        text = self.task_adding.text()
        self.task_adding.clear()
        self.list.addItem(text)

    def remove_task(self, item):
        self.list.takeItem(self.list.row(item))


app = QApplication()
main_window = MainWindow()
main_window.show()

# Execute the application

app.exec()
