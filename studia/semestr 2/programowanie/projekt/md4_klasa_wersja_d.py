import struct
import hashlib


class MD4:
    def __init__(self):
        self.h0 = 0x67452301
        self.h1 = 0xEFCDAB89
        self.h2 = 0x98BADCFE
        self.h3 = 0x10325476
        self.buffer = b""
        self.bytes = 0

    def _left_rotate(self, n, b):
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def _process_block(self, block):
        x = list(struct.unpack("<16I", block) + (None,) * (80 - 16))
        a = self.h0
        b = self.h1
        c = self.h2
        d = self.h3

        # Round 1
        for i in range(16):
            k = i
            s = [3, 7, 11, 19][i % 4]
            a = self._left_rotate((a + ((b & c) | (~b & d)) + x[k]) & 0xFFFFFFFF, s)

        # Round 2
        for i in range(16):
            k = (i * 5 + 1) % 16
            s = [3, 5, 9, 13][i % 4]
            a = self._left_rotate((a + ((b & c) | (b & d) | (c & d)) + x[k] + 0x5A827999) & 0xFFFFFFFF, s)

        # Round 3
        for i in range(16):
            k = (i * 3 + 5) % 16
            s = [3, 9, 11, 15][i % 4]
            a = self._left_rotate((a + (b ^ c ^ d) + x[k] + 0x6ED9EBA1) & 0xFFFFFFFF, s)

        self.h0 = (self.h0 + a) & 0xFFFFFFFF
        self.h1 = (self.h1 + b) & 0xFFFFFFFF
        self.h2 = (self.h2 + c) & 0xFFFFFFFF
        self.h3 = (self.h3 + d) & 0xFFFFFFFF

    def update(self, data):
        self.bytes += len(data)
        self.buffer += data

        while len(self.buffer) >= 64:
            self._process_block(self.buffer[:64])
            self.buffer = self.buffer[64:]

    def finalize(self):
        pad = b"\x80" + b"\x00" * ((56 - (self.bytes + 1) % 64) % 64)
        length_bits = struct.pack("<Q", self.bytes * 8)
        self.update(pad + length_bits)

    def hexdigest(self):
        self.finalize()
        return "%08x%08x%08x%08x" % (self.h0, self.h1, self.h2, self.h3)

    def digest(self):
        self.finalize()
        return struct.pack("<4I", self.h0, self.h1, self.h2, self.h3)

    def array(self):
        return list(struct.unpack("<4I", self.digest()))

    def array_buffer(self):
        return self.digest()

    def buffer(self):
        return self.array_buffer()


# Przykładowe użycie:
data = b"Ala ma kota"
md4 = MD4()     
md4.update(data)
print(md4.hexdigest())
