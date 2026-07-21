import struct
from typing import List

class MD4():
    start_table = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    def __init__(self, x: bytes):
        self.x = x
        x += b"\x80"
        x += b"\x00" * (-(len(x) + 8) % 64)
        x += struct.pack("<Q", len(self.x) * 8)
        self.hash = self.get_hash([x[i : i + 64] for i in range(0, len(x), 64)])
    
    @classmethod
    def from_string(cls, x: str):
        return cls(x.encode())

    @classmethod
    def from_file(cls, x):
        with open(x, mode="rb") as file:
            file_content = file.read()
        return cls(file_content)
        
    @classmethod
    def get_hash(cls, fragment) -> List[int]:
        const_values = [
            ("F", 0x00000000, 0, 0x03), ("F", 0x00000000, 1, 0x07), ("F", 0x00000000, 2, 0x0B), ("F", 0x00000000, 3, 0x13),
            ("F", 0x00000000, 4, 0x03), ("F", 0x00000000, 5, 0x07), ("F", 0x00000000, 6, 0x0B), ("F", 0x00000000, 7, 0x13),
            ("F", 0x00000000, 8, 0x03), ("F", 0x00000000, 9, 0x07), ("F", 0x00000000, 10, 0x0B), ("F", 0x00000000, 11, 0x13),
            ("F", 0x00000000, 12, 0x03), ("F", 0x00000000, 13, 0x07), ("F", 0x00000000, 14, 0x0B), ("F", 0x00000000, 15, 0x13),
            ("G", 0x5A827999, 0, 0x03), ("G", 0x5A827999, 4, 0x05), ("G", 0x5A827999, 8, 0x09), ("G", 0x5A827999, 12, 0x0D),
            ("G", 0x5A827999, 1, 0x03), ("G", 0x5A827999, 5, 0x05), ("G", 0x5A827999, 9, 0x09), ("G", 0x5A827999, 13, 0x0D),
            ("G", 0x5A827999, 2, 0x03), ("G", 0x5A827999, 6, 0x05), ("G", 0x5A827999, 10, 0x09), ("G", 0x5A827999, 14, 0x0D),
            ("G", 0x5A827999, 3, 0x03), ("G", 0x5A827999, 7, 0x05), ("G", 0x5A827999, 11, 0x09), ("G", 0x5A827999, 15, 0x0D),
            ("H", 0x6ED9EBA1, 0, 0x03), ("H", 0x6ED9EBA1, 8, 0x09), ("H", 0x6ED9EBA1, 4, 0x0B), ("H", 0x6ED9EBA1, 12, 0x0F),
            ("H", 0x6ED9EBA1, 2, 0x03), ("H", 0x6ED9EBA1, 10, 0x09), ("H", 0x6ED9EBA1, 6, 0x0B), ("H", 0x6ED9EBA1, 14, 0x0F),
            ("H", 0x6ED9EBA1, 1, 0x03), ("H", 0x6ED9EBA1, 9, 0x09), ("H", 0x6ED9EBA1, 5, 0x0B), ("H", 0x6ED9EBA1, 13, 0x0F),
            ("H", 0x6ED9EBA1, 3, 0x03), ("H", 0x6ED9EBA1, 11, 0x09), ("H", 0x6ED9EBA1, 7, 0x0B), ("H", 0x6ED9EBA1, 15, 0x0F)
        ]
        for part in fragment:
            X = list(struct.unpack("<16I", part))
            a, b, c, d = cls.start_table

            for i in range(48):
                if const_values[i][0] == "F":
                    f = lambda x, y, z: (x & y) | (~x & z)
                elif const_values[i][0] == "G":
                    f = lambda x, y, z: ((x & y) | (y & z) | (x & z))
                else:
                    f = lambda x, y, z: (x ^ y ^ z)

                a_temp = a
                b_temp = b
                c_temp = c
                d_temp = d
                a = d_temp
                b = cls.left_rotate((a_temp + f(b_temp, c_temp, d_temp) + X[const_values[i][2]] + const_values[i][1]) % (2 ** 32), const_values[i][3])
                c = b_temp
                d = c_temp
 
        hash_ = [a,b,c,d]
        return [((temp_1 + temp_2) % (2 ** 32)) for temp_1, temp_2 in zip(cls.start_table,hash_)]
    
    @staticmethod
    def left_rotate(value, n):
        return (value << n)  % (2 ** 32) | value >> (32 - n)
    
    def __str__(self) -> str:
        return MD4(self.x)._hex()
        
    def _hex(cls):
        return "".join(f"{value:02x}" for value in cls._bytes())
    
    def _bytes(cls):
        return struct.pack("<4L", *cls.hash)
    

import random

class RSA:
    def __init__(self,public_key = None,private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    def generate_keypair(self):
        p = self.generate_prime_number()
        q = self.generate_prime_number()

        n = p * q
        phi_n = (p - 1) * (q - 1)

        e = self.choose_coprime(phi_n)
        d = self.modular_inverse(e, phi_n)

        self.public_key = (e, n)
        self.private_key = (d, n)

    @staticmethod
    def generate_prime_number():
        while True:
            num = random.randint(2**10, 2**11)
            if RSA.is_prime(num):
                return num

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def choose_coprime(phi_n):
        while True:
            e = random.randint(2, phi_n)
            if RSA.nwd(e, phi_n) == 1:
                return e

    @staticmethod
    def nwd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def modular_inverse(a, m):
        g, x, _ = RSA.extended_nwd(a, m)
        if g != 1:
            raise ValueError("Błąd w obliczeniach")
        return x % m

    @staticmethod
    def extended_nwd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = RSA.extended_nwd(b % a, a)
        return g, y - (b // a) * x, x

    def encode(self, text):
        if self.public_key is None:
            raise ValueError("Nie wygenerowano klucza")

        e, n = self.public_key
        hash_text = [pow(ord(char), e, n) for char in text]
        return hash_text

    def decode(self, hash_text):
        if self.private_key is None:
            raise ValueError("Nie wygenerowano klucza")

        d, n = self.private_key
        text = ''.join([chr(pow(char, d, n)) for char in hash_text])
        return text


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QDialog, QWidget, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prosty szablon z przyciskami")
        self.resize(450, 300)

        self.main_layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_layout)

        self.button1 = QPushButton("Wczytaj wiadość")
        self.button1.clicked.connect(lambda: self.show_task1_options())
        self.main_layout.addWidget(self.button1)

        self.button2 = QPushButton("Utworz klucz")
        self.button2.clicked.connect(lambda: self.task_2())
        self.main_layout.addWidget(self.button2)

        self.button3 = QPushButton("Wyswietl klucz publiczny")
        self.button3.clicked.connect(lambda: self.task_3())
        self.main_layout.addWidget(self.button3)

        self.button3p = QPushButton("Wyswietl klucz prywatny")
        self.button3p.clicked.connect(lambda: self.task_3p())
        self.main_layout.addWidget(self.button3p)

        self.button4 = QPushButton("Zakoduj widomość MD4")
        self.button4.clicked.connect(lambda: self.task_4(md4_digest))
        self.main_layout.addWidget(self.button4)
        
        self.button5 = QPushButton("Zaszyfruj widomość RSA")
        self.button5.clicked.connect(lambda: self.task_5(md4_digest))
        self.main_layout.addWidget(self.button5)

        self.button6 = QPushButton("Odszyfruj widomość RSA")
        self.button6.clicked.connect(lambda: self.task_6())
        self.main_layout.addWidget(self.button6)

    def show_task1_options(self):
        options_dialog = QDialog(self)
        options_dialog.setWindowTitle("Importuj wiadomość z")
        options_layout = QVBoxLayout()
        options_dialog.setLayout(options_layout)

        option1_button = QPushButton("Wprowadz ręcznie")
        option1_button.clicked.connect(lambda: self.task_1())
        options_layout.addWidget(option1_button)

        option2_button = QPushButton("Pobierz z pliku")
        option2_button.clicked.connect(lambda: self.task_1p())
        options_layout.addWidget(option2_button)

        options_dialog.exec_()

    def task_1(self):
        global md4_digest
        text, ok = QLineEdit.getText(QLineEdit(), "Wprowadź wiadomość")
        if ok:
            md4_digest = MD4.from_string(text)
            result_window = ResultWindow("Wczytano wiadomość")
            result_window.exec_()

    def task_1p(self):
        global md4_digest
        md4_digest = MD4.from_file('C:\\Users\\micha\\OneDrive\\Dokumenty\\projekty-python\\studia\\semestr 2\\programowanie\\projekt\\wiadomosc.txt')
        result_window = ResultWindow("Wczytano z pliku")
        result_window.exec_()

    def task_2(self):
        rsa.generate_keypair()
        result_window = ResultWindow("Pomyślnie utworzono parę kluczy")
        result_window.exec_()

    def task_3(self):
        result_window = ResultWindow(str(rsa.public_key))
        result_window.exec_()
        
    def task_3p(self):
        result_window = ResultWindow(str(rsa.private_key))
        result_window.exec_()

    def task_4(self, md4_digest):
        result_window = ResultWindow(str(md4_digest))
        result_window.exec_()

    def task_5(self, md4_digest):
        global encrypted_message
        encrypted_message = rsa.encode(str(md4_digest.x))
        result_window = ResultWindow(str(encrypted_message))
        result_window.exec_()

    def task_6(self):
        decrypted_message = rsa.decode(encrypted_message)
        result_window = ResultWindow(str(decrypted_message))
        result_window.exec_()


class ResultWindow(QDialog):
    def __init__(self, result_text):
        super().__init__()
        self.setWindowTitle("Wynik")
        self.resize(400, 100)

        self.result_label = QLabel(result_text, self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setGeometry(1, 1, 260, 60)

        self.back_button = QPushButton("Powrót do menu", self)
        self.back_button.setGeometry(60, 70, 80, 20)
        self.back_button.clicked.connect(self.close)

encrypted_message = ''
md4_digest = "nie wczytano wiadomości"
rsa = RSA()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
