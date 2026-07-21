import struct
import sys

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def md4(message):
    message = bytearray(message)
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += struct.pack("<Q", orig_len_in_bits)

    h0 = 0x67452301
    h1 = 0xefcdab89
    h2 = 0x98badcfe
    h3 = 0x10325476

    def F(x, y, z):
        return ((x & y) | (~x & z))

    def G(x, y, z):
        return ((x & y) | (x & z) | (y & z))

    def H(x, y, z):
        return (x ^ y ^ z)

    def FF(a, b, c, d, x, s):
        a = left_rotate((a + F(b, c, d) + x) & 0xFFFFFFFF, s)
        return a

    def GG(a, b, c, d, x, s):
        a = left_rotate((a + G(b, c, d) + x + 0x5A827999) & 0xFFFFFFFF, s)
        return a

    def HH(a, b, c, d, x, s):
        a = left_rotate((a + H(b, c, d) + x + 0x6ED9EBA1) & 0xFFFFFFFF, s)
        return a

    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        a = h0
        b = h1
        c = h2
        d = h3

        x = []
        for j in range(0, 64, 4):
            x.append(struct.unpack("<I", chunk[j:j+4])[0])

        for j in range(16):
            a = FF(a, b, c, d, x[j], round_constants[j][3])

        for j in range(16):
            a = GG(a, b, c, d, x[(5*j + 1) % 16], round_constants[16+j][3])

        for j in range(16):
            a = HH(a, b, c, d, x[(3*j + 5) % 16], round_constants[32+j][3])

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    return struct.pack("<I", h0) + struct.pack("<I", h1) + struct.pack("<I", h2) + struct.pack("<I", h3)

# Round Constants
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
    (0, "G", 1518500249, 3),
    (1, "G", 1518500249, 5),
    (2, "G", 1518500249, 9),
    (3, "G", 1518500249, 13),
    (4, "G", 1518500249, 3),
    (5, "G", 1518500249, 5),
    (6, "G", 1518500249, 9),
    (7, "G", 1518500249, 13),
    (8, "G", 1518500249, 3),
    (9, "G", 1518500249, 5),
    (10, "G", 1518500249, 9),
    (11, "G", 1518500249, 13),
    (12, "G", 1518500249, 3),
    (13, "G", 1518500249, 5),
    (14, "G", 1518500249, 9),
    (15, "G", 1518500249, 13),

    # Runda 3
    (0, "H", 1859775393, 3),
    (1, "H", 1859775393, 9),
    (2, "H", 1859775393, 11),
    (3, "H", 1859775393, 15),
    (4, "H", 1859775393, 3),
    (5, "H", 1859775393, 9),
    (6, "H", 1859775393, 11),
    (7, "H", 1859775393, 15),
    (8, "H", 1859775393, 3),
    (9, "H", 1859775393, 9),
    (10, "H", 1859775393, 11),
    (11, "H", 1859775393, 15),
    (12, "H", 1859775393, 3),
    (13, "H", 1859775393, 9),
    (14, "H", 1859775393, 11),
    (15, "H", 1859775393, 15)
]

message = "Ala ma kota"
digest = md4(message.encode())
print("Message:", message)
print("MD4 Digest:", digest.hex())
