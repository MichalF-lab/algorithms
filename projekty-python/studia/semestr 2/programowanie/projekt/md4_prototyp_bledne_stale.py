import struct

# Stałe rundy
round_constants = [
    # Runda 1
    (0, "F", 0, 3),
    (1, "F", 0, 7),
    (2, "F", 0, 11),
    (3, "F", 0, 19),
    (4, "F", 1, 3),
    (5, "F", 1, 7),
    (6, "F", 1, 11),
    (7, "F", 1, 19),
    (8, "F", 2, 3),
    (9, "F", 2, 7),
    (10, "F", 2, 11),
    (11, "F", 2, 19),
    (12, "F", 3, 3),
    (13, "F", 3, 7),
    (14, "F", 3, 11),
    (15, "F", 3, 19),

    # Runda 2
    (0, "G", 0x5A827999, 3),
    (1, "G", 0x5A827999, 5),
    (2, "G", 0x5A827999, 9),
    (3, "G", 0x5A827999, 13),
    (4, "G", 0x6ED9EBA1, 3),
    (5, "G", 0x6ED9EBA1, 5),
    (6, "G", 0x6ED9EBA1, 9),
    (7, "G", 0x6ED9EBA1, 13),
    (8, "G", 0x8F1BBCDC, 3),
    (9, "G", 0x8F1BBCDC, 5),
    (10, "G", 0x8F1BBCDC, 9),
    (11, "G", 0x8F1BBCDC, 13),
    (12, "G", 0xA953FD4E, 3),
    (13, "G", 0xA953FD4E, 5),
    (14, "G", 0xA953FD4E, 9),
    (15, "G", 0xA953FD4E, 13),

    # Runda 3
    (0, "H", 0x6ED9EBA1, 3),
    (1, "H", 0x6ED9EBA1, 9),
    (2, "H", 0x6ED9EBA1, 11),
    (3, "H", 0x6ED9EBA1, 15),
    (4, "H", 0x8F1BBCDC, 3),
    (5, "H", 0x8F1BBCDC, 9),
    (6, "H", 0x8F1BBCDC, 11),
    (7, "H", 0x8F1BBCDC, 15),
    (8, "H", 0xA953FD4E, 3),
    (9, "H", 0xA953FD4E, 9),
    (10, "H", 0xA953FD4E, 11),
    (11, "H", 0xA953FD4E, 15),
    (12, "H", 0x6ED9EBA1, 3),
    (13, "H", 0x6ED9EBA1, 9),
    (14, "H", 0x6ED9EBA1, 11),
    (15, "H", 0x6ED9EBA1, 15)
]

# Funkcje pomocnicze
def F(x, y, z):
    return (x & y) | ((~x) & z)

def G(x, y, z):
    return (x & y) | (x & z) | (y & z)

def H(x, y, z):
    return x ^ y ^ z

# Funkcja kompresji MD4
def MD4Compression(A, B, C, D, M):
    for i in range(len(round_constants)):
        idx, f, y, w = round_constants[i]
        if f == "F":
            temp = F(B, C, D)
        elif f == "G":
            temp = G(B, C, D)
        elif f == "H":
            temp = H(B, C, D)

        temp = (A + temp + M[idx]) & 0xFFFFFFFF
        temp = temp << w | temp >> (32 - w)

        A, B, C, D = D, temp, B, C

    return (A & 0xFFFFFFFF, B & 0xFFFFFFFF, C & 0xFFFFFFFF, D & 0xFFFFFFFF)

# Funkcja pomocnicza do konwersji wiadomości na listę 32-bitowych słów
def process_message(message):
    message = bytearray(message)
    length = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += struct.pack("<Q", length)
    return struct.unpack("<" + "I" * (len(message) // 4), message)

# Funkcja haszująca MD4
def MD4Hash(message):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    M = process_message(message)
    return MD4Compression(A, B, C, D, M)

# Przykładowe użycie
message = "Ala ma kota"
hash_value = MD4Hash(message.encode())
hash_str = ''.join('%08x' % i for i in hash_value)
print(hash_str)
