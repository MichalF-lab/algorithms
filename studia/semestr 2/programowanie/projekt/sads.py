import struct

def F(x, y, z):
    return (x & y) | (~x & z)

def G(x, y, z):
    return (x & y) | (x & z) | (y & z)

def H(x, y, z):
    return x ^ y ^ z

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF
    

class MD4:
    def __init__(self, message=None):
        self.h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476
        ]
        self.message = message
        self.finalized = False

    def pad_message(self):
        length = len(self.message)
        padding = b'\x80' + b'\x00' * ((56 - (length + 1) % 64) % 64)
        length_bits = struct.pack('<Q', length * 8)
        padded_message = self.message.encode() + padding + length_bits
        return padded_message

    def process_block(self, block):
        x = list(struct.unpack('<16I', block))

        a, b, c, d = self.h

        # Round 1
        for i in range(16):
            k = i
            s = [3, 7, 11, 19][i % 4]
            a = left_rotate((a + F(b, c, d) + x[k]) & 0xFFFFFFFF, s)
            a &= 0xFFFFFFFF
            a, b, c, d = d, a, b, c

        # Round 2
        for i in range(16):
            k = (i * 4 + 3) % 16
            s = [3, 5, 9, 13][i % 4]
            a = left_rotate((a + G(b, c, d) + x[k] + 0x5A827999) & 0xFFFFFFFF, s)
            a &= 0xFFFFFFFF
            a, b, c, d = d, a, b, c

        # Round 3
        for i in range(16):
            k = (i * 4 + 7) % 16
            s = [3, 9, 11, 15][i % 4]
            a = left_rotate((a + H(b, c, d) + x[k] + 0x6ED9EBA1) & 0xFFFFFFFF, s)
            a &= 0xFFFFFFFF
            a, b, c, d = d, a, b, c

        self.h[0] = (self.h[0] + a) & 0xFFFFFFFF
        self.h[1] = (self.h[1] + b) & 0xFFFFFFFF
        self.h[2] = (self.h[2] + c) & 0xFFFFFFFF
        self.h[3] = (self.h[3] + d) & 0xFFFFFFFF

    def update(self, message):
        if self.finalized:
            raise ValueError("Cannot update finalized hash object")
        self.message += message

    def finalize(self):
        if self.finalized:
            return

        padded_message = self.pad_message()

        for i in range(0, len(padded_message), 64):
            block = padded_message[i:i+64]
            self.process_block(block)
            self.finalized = True

    def hexdigest(self):
        if not self.finalized:
            raise ValueError("Cannot get hex digest from non-finalized hash object")

        return ''.join(format(h, '08x') for h in self.h)

def md4(message):
    md4_obj = MD4(message)
    md4_obj.finalize()
    return md4_obj.hexdigest()

message = "Hello, world!"
digest = md4(message)
print(digest)
