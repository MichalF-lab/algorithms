import struct
from typing import List

class MD4():
    start_table = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    def __init__(self, x: bytes):
        self.x = x
        x += b"\x80"
        x += b"\x00" * (-(len(x) + 8) % 64)
        x += struct.pack("<Q", len(self.x) * 8)
        self.hash = self.get_hash([x[i : i + 64] for i in range(0, len(x), 64)])
    
    @classmethod
    def from_string(cls, x: str):
        return cls(x.encode())

    @classmethod
    def from_file(cls, x):
        with open(x, mode="rb") as file:
            file_content = file.read()
        return cls(file_content)
        
    @classmethod
    def get_hash(cls, fragment) -> List[int]:
        const_values = [
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
        for part in fragment:
            X = list(struct.unpack("<16I", part))
            a, b, c, d = cls.start_table

            for i in range(48):
                if const_values[i][0] == "F":
                    f = lambda x, y, z: (x & y) | (~x & z)
                elif const_values[i][0] == "G":
                    f = lambda x, y, z: ((x & y) | (y & z) | (x & z))
                else:
                    f = lambda x, y, z: (x ^ y ^ z)

                a_temp = a
                b_temp = b
                c_temp = c
                d_temp = d
                a = d_temp
                b = cls.left_rotate((a_temp + f(b_temp, c_temp, d_temp) + X[const_values[i][2]] + const_values[i][1]) % (2 ** 32), const_values[i][3])
                c = b_temp
                d = c_temp
 
        hash_ = [a,b,c,d]
        return [((temp_1 + temp_2) % (2 ** 32)) for temp_1, temp_2 in zip(cls.start_table,hash_)]
    
    @staticmethod
    def left_rotate(value, n):
        return (value << n)  % (2 ** 32) | value >> (32 - n)
    
    def __str__(self) -> str:
        return MD4(self.x)._hex()
        
    def _hex(cls):
        return "".join(f"{value:02x}" for value in cls._bytes())
    
    def _bytes(cls):
        return struct.pack("<4L", *cls.hash)
    
md4_digest = MD4.from_file('studia\semestr 2\programowanie\testy\wiadomosc.txt')
print(md4_digest)