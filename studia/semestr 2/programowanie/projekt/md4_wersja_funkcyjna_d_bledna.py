import struct


# Stałe używane w funkcji kompresji
round_constants = [
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

# Stałe początkowe
initial_state = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

# ---------------------------Do tąd jest git--------------------------------------------------------------

# Funkcja kompresji
def compression_function(state, message_block):
    a, b, c, d = state

    for i in range(48):
        if i < 16:
            f = lambda x, y, z: (x & y) | (~x & z)
        elif i < 32:
            f = lambda x, y, z: (x & y) | (x & z) | (y & z)
        else:
            f = lambda x, y, z: x ^ y ^ z

        d_temp = d
        b = left_rotate((a + f(b, c, d) + message_block[round_constants[i][2]] + round_constants[i][1]) % (2 ** 32), round_constants[i][3])
        a = d_temp
        d = c
        c = b

    # state[0] = (state[0] + a) % (2 ** 32)
    # state[1] = (state[1] + b) % (2 ** 32)
    # state[2] = (state[2] + c) % (2 ** 32)
    # state[3] = (state[3] + d) % (2 ** 32)

    # struct.pack(”<Q”, n)
    state[0] = struct.pack('<Q', a)
    state[1] = struct.pack('<Q', b)
    state[2] = struct.pack('<Q', c)
    state[3] = struct.pack('<Q', d)


# Funkcja pomocnicza do rotacji bitów w lewo GIT
def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) % (2 ** 32)


# Funkcja generująca skrót MD4
def md4(message):
    # Konwersja wiadomości na tablicę 32-bitowych wartości
    message = bytearray(message, 'utf-8')
    message_length = len(message) * 8

    # Dodanie paddingu
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)

    # Dodanie długości wiadomości na końcu
    message += struct.pack('<Q', message_length)

    # Inicjalizacja stanu
    state = initial_state.copy()

    # Podział wiadomości na bloki 512-bitowe
    message_blocks = [message[i:i + 64] for i in range(0, len(message), 64)]
    

    # Kompresja każdego bloku
    for block in message_blocks:
        block_words = list(struct.unpack('<16I', block))
        compression_function(state, block_words)

    # Konwersja stanu na ciąg bajtów reprezentujący skrót
    digest = b''.join(struct.pack('<I', word) for word in struct.unpack('>Q',state))
    return digest.hex()


# Przykładowe użycie
message = "Ala ma kota"
md4_digest = md4(message)
print("MD4 digest:", md4_digest)
