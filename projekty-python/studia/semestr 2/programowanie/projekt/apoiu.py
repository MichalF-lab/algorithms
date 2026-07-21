import struct


class MD4:
    INITIAL_STATE = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    def __init__(self, message):
        self.message = message
        self.padded_message = self._pad_message(message)
        self.hash = self._calculate_hash()

    @staticmethod
    def _pad_message(message):
        message_length = len(message)
        pad_length = (56 - (message_length + 1) % 64) % 64
        padded_message = message + b'\x80' + b'\x00' * pad_length
        padded_message += struct.pack('<Q', message_length * 8)
        return padded_message

    def _calculate_hash(self):
        state = self.INITIAL_STATE.copy()
        chunks = [self.padded_message[i:i + 64] for i in range(0, len(self.padded_message), 64)]

        for chunk in chunks:
            words = list(struct.unpack('<16I', chunk))
            a, b, c, d = state

            for i in range(16):
                if i < 4:
                    f = (b & c) | (~b & d)
                    g = i
                elif i < 8:
                    f = (b & (c | d)) | (c & d)
                    g = (5 * i + 1) % 16
                elif i < 12:
                    f = b ^ c ^ d
                    g = (3 * i + 5) % 16
                else:
                    f = c ^ (b | ~d)
                    g = (7 * i) % 16

                temp = d
                d = c
                c = b
                b = (b + self._left_rotate((a + f + words[g]) & 0xFFFFFFFF, [3, 7, 11, 19][i % 4])) & 0xFFFFFFFF
                a = temp

            state[0] = (state[0] + a) & 0xFFFFFFFF
            state[1] = (state[1] + b) & 0xFFFFFFFF
            state[2] = (state[2] + c) & 0xFFFFFFFF
            state[3] = (state[3] + d) & 0xFFFFFFFF

        return struct.pack('<4I', *state)

    @staticmethod
    def _left_rotate(value, shift):
        return ((value << shift) & 0xFFFFFFFF) | (value >> (32 - shift))

    def __str__(self):
        return self.hash.hex()


message = b"Ala ma kota"
md4_digest = MD4(message)
print(md4_digest)
