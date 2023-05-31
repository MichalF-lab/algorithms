import struct


# Stałe używane w funkcji kompresji
round_constants = []
round1 = [("F", 0, 0, 3), ("F", 0, 1, 7), ("F", 0, 2, 11), ("F", 0, 3, 19),
        ("F", 0, 4, 3), ("F", 0, 5, 7), ("F", 0, 6, 11), ("F", 0, 7, 19),
        ("F", 0, 8, 3), ("F", 0, 9, 7), ("F", 0, 10, 11), ("F", 0, 11, 19),
        ("F", 0, 12, 3), ("F", 0, 13, 7), ("F", 0, 14, 11), ("F", 0, 15, 19)]

round2 = [("G", 1518500249, 0, 3), ("G", 1518500249, 4, 5), ("G", 1518500249, 8, 9), ("G", 1518500249, 12, 13),
        ("G", 1518500249, 1, 3), ("G", 1518500249, 5, 5), ("G", 1518500249, 9, 9), ("G", 1518500249, 13, 13),
        ("G", 1518500249, 2, 3), ("G", 1518500249, 6, 5), ("G", 1518500249, 10, 9), ("G", 1518500249, 14, 13),
        ("G", 1518500249, 3, 3), ("G", 1518500249, 7, 5), ("G", 1518500249, 11, 9), ("G", 1518500249, 15, 13)]

round3 = [("H", 1859775393, 0, 3), ("H", 1859775393, 8, 9), ("H", 1859775393, 4, 11), ("H", 1859775393, 12, 15),
        ("H", 1859775393, 2, 3), ("H", 1859775393, 10, 9), ("H", 1859775393, 6, 11), ("H", 1859775393, 14, 15),
        ("H", 1859775393, 1, 3), ("H", 1859775393, 9, 9), ("H", 1859775393, 5, 11), ("H", 1859775393, 13, 15),
        ("H", 1859775393, 3, 3), ("H", 1859775393, 11, 9), ("H", 1859775393, 7, 11), ("H", 1859775393, 15, 15)]

round_constants.extend(round1)
round_constants.extend(round2)
round_constants.extend(round3)

# Stałe początkowe
initial_state = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]


# Funkcja kompresji
def compression_function(state, message_block):
    a, b, c, d = state

    for i in range(48):
        if i < 16:
            f = lambda x, y, z: (x & y) | (~x & z)
            g = i
        elif i < 32:
            f = lambda x, y, z: (x & y) | (x & z) | (y & z)
            g = (5 * i + 1) % 16
        else:
            f = lambda x, y, z: x ^ y ^ z
            g = (3 * i + 5) % 16

        d_temp = d
        d = c
        c = b
        b = b + left_rotate((a + f(b, c, d) + message_block[g]) % (2 ** 32), round_constants[i][2])
        a = d_temp

    state[0] = (state[0] + a) % (2 ** 32)
    state[1] = (state[1] + b) % (2 ** 32)
    state[2] = (state[2] + c) % (2 ** 32)
    state[3] = (state[3] + d) % (2 ** 32)


# Funkcja pomocnicza do rotacji bitów w lewo
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
        block_words = struct.unpack('<16I', block)
        compression_function(state, list(block_words))

    # Konwersja stanu na ciąg bajtów reprezentujący skrót
    digest = b''.join(struct.pack('<I', word) for word in state)
    return digest.hex()


# Przykładowe użycie
message = "Ala ma kota"
md4_digest = md4(message)
print("MD4 digest:", md4_digest)
