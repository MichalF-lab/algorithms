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

# Przykład użycia:
rsa = RSA()

# Generowanie kluczy
rsa.generate_keypair()

# Szyfrowanie wiadomości
message = "Witaj swiecie"
encrypted_message = rsa.encode(message)

# Deszyfrowanie zaszyfrowanej wiadomości
decrypted_message = rsa.decode(encrypted_message)

# Wyświetlanie wyników
print("Klucz publiczny:", rsa.public_key)
print("Klucz prywatny:", rsa.private_key)
print("Zaszyfrowana wiadomosc:", encrypted_message)
print("Odszyfrowana wiadomosc:", decrypted_message)
