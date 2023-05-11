import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Podpisy cyfrowe")
        self.resize(400, 300)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.button1 = QPushButton("Przycisk 1")
        self.button1.clicked.connect(lambda: self.task_1())
        self.main_layout.addWidget(self.button1)

        self.button2 = QPushButton("Przycisk 2")
        self.button2.clicked.connect(lambda: self.task_2())
        self.main_layout.addWidget(self.button2)

        self.button3 = QPushButton("Przycisk 3")
        self.button3.clicked.connect(lambda: self.task_3())
        self.main_layout.addWidget(self.button3)

        self.button4 = QPushButton("Przycisk 4")
        self.button4.clicked.connect(lambda: self.task_4())
        self.main_layout.addWidget(self.button4)

    def task_1(self):
        #Do Something
        result_window = ResultWindow("Wynik / wykonano zad 1", self)
        result_window.show()
    
    def task_2(self):
        #Do Something
        result_window = ResultWindow("Wynik / wykonano zad 2", self)
        result_window.show()
    
    def task_3(self):
        #Do Something
        result_window = ResultWindow("Wynik / wykonano zad 3", self)
        result_window.show()
    
    def task_4(self):
        #Do Something
        result_window = ResultWindow("Wynik / wykonano zad 4", self)
        result_window.show()

class ResultWindow(QWidget):
    def __init__(self, result_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Wynik")
        self.resize(200, 100)

        self.layout = QVBoxLayout(self)
        self.result_label = QLabel(result_text, self)
        self.layout.addWidget(self.result_label)

        self.back_button = QPushButton("wyczyść wynik", self)
        self.back_button.clicked.connect(self.close)
        self.layout.addWidget(self.back_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
