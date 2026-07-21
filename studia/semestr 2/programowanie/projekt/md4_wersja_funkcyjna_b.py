import struct
import hashlib


def md4(message):
    # Padding
    padding = b'\x80'
    message_length = len(message)
    pad_length = (56 - message_length % 64) % 64
    padding += b'\x00' * pad_length
    message += padding + struct.pack('<Q', message_length * 8)

    # Initialization
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476

    # Main loop
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]

        x = list(struct.unpack('<16I', chunk))

        a = h0
        b = h1
        c = h2
        d = h3

        # Round 1
        def F(x, y, z): return (x & y) | (~x & z)
        for i in range(16):
            k = i
            temp = left_rotate((a + F(b, c, d) + x[k]) & 0xFFFFFFFF, [3, 7, 11, 19][i % 4])
            a, b, c, d = d, temp, b, c

        # Round 2
        def G(x, y, z): return (x & y) | (x & z) | (y & z)
        for i in range(16):
            k = (i * 5 + 1) % 16
            temp = left_rotate((a + G(b, c, d) + x[k] + 0x5A827999) & 0xFFFFFFFF, [3, 5, 9, 13][i % 4])
            a, b, c, d = d, temp, b, c

        # Round 3
        def H(x, y, z): return x ^ y ^ z
        for i in range(16):
            k = (i * 3 + 5) % 16
            temp = left_rotate((a + H(b, c, d) + x[k] + 0x6ED9EBA1) & 0xFFFFFFFF, [3, 9, 11, 15][i % 4])
            a, b, c, d = d, temp, b, c

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    # Digest
    digest = struct.pack('<4I', h0, h1, h2, h3)
    return digest.hex()


def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


# Test
message = "Ala ma kota"
digest = md4(message.encode('utf-8'))
print(digest)
