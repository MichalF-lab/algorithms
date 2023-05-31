import struct
# Stałe rundy
round_constants = [
    # Runda 1
    (0, "F", 0, 3),
    (1, "F", 0, 7),
    (2, "F", 0, 11),
    (3, "F", 0, 19),
    (4, "F", 0, 3),
    (5, "F", 0, 7),
    (6, "F", 0, 11),
    (7, "F", 0, 19),
    (8, "F", 0, 3),
    (9, "F", 0, 7),
    (10, "F", 0, 11),
    (11, "F", 0, 19),
    (12, "F", 0, 3),
    (13, "F", 0, 7),
    (14, "F", 0, 11),
    (15, "F", 0, 19),

    # Runda 2
    (16, "G", 1518500249, 3),
    (17, "G", 1518500249, 5),
    (18, "G", 1518500249, 9),
    (19, "G", 1518500249, 13),
    (20, "G", 1518500249, 3),
    (21, "G", 1518500249, 5),
    (22, "G", 1518500249, 9),
    (23, "G", 1518500249, 13),
    (24, "G", 1518500249, 3),
    (25, "G", 1518500249, 5),
    (26, "G", 1518500249, 9),
    (27, "G", 1518500249, 13),
    (28, "G", 1518500249, 3),
    (29, "G", 1518500249, 5),
    (30, "G", 1518500249, 9),
    (31, "G", 1518500249, 13),

    # Runda 3
    (32, "H", 1859775393, 3),
    (33, "H", 1859775393, 9),
    (34, "H", 1859775393, 11),
    (35, "H", 1859775393, 15),
    (36, "H", 1859775393, 3),
    (37, "H", 1859775393, 9),
    (38, "H", 1859775393, 11),
    (39, "H", 1859775393, 15),
    (40, "H", 1859775393, 3),
    (41, "H", 1859775393, 9),
    (42, "H", 1859775393, 11),
    (43, "H", 1859775393, 15),
    (44, "H", 1859775393, 3),
    (45, "H", 1859775393, 9),
    (46, "H", 1859775393, 11),
    (47, "H", 1859775393, 15)
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

        temp = (A + temp + M[idx] + y) & 0xFFFFFFFF
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
message = "Hello, world!"
hash_value = MD4Hash(message.encode())
print(hash_value)