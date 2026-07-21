import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QDialog, QWidget
from PyQt5.QtCore import Qt

# Import z innego pliku
import MD4

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prosty szablon z przyciskami")
        self.resize(400, 300)

        self.main_layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_layout)

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
        result_window = ResultWindow("Wynik / wykonano zad 1")
        result_window.exec_()
    
    def task_2(self):
        #Do Something
        result_window = ResultWindow("Wynik / wykonano zad 2")
        result_window.exec_()
    
    def task_3(self):
        #Do Something
        result_window = ResultWindow("Wynik / wykonano zad 3")
        result_window.exec_()
    
    def task_4(self):
        #Do Something
        result_window = ResultWindow("Wynik / wykonano zad 4")
        result_window.exec_()


class ResultWindow(QDialog):
    def __init__(self, result_text):
        super().__init__()
        self.setWindowTitle("Wynik")
        self.resize(200, 100)

        self.result_label = QLabel(result_text, self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setGeometry(10, 10, 180, 50)

        self.back_button = QPushButton("Powrót do menu", self)
        self.back_button.setGeometry(60, 70, 80, 20)
        self.back_button.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
