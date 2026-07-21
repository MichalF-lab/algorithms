import struct
from typing import List

class MD4():
    start_table = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    def __init__(self, x: bytes):
        self.x = x
        self.hash = self.get_hash(...)
    
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

        a, b, c, d = cls.start_table

        b = cls.left_rotate(...)

        hash_ = [a,b,c,d]
        return [((v + n) % (2 ** 32)) for v, n in zip(cls.start_table,hash_)]
    
    @staticmethod
    def left_rotate(value, n):
        return (...)
    
    def __str__(self) -> str:
        return MD4(message)._hex()
        
    def _hex(cls):
        return "".join(f"{value:02x}" for value in cls._bytes())

    def _bytes(cls):
        return struct.pack("<4L", *cls.hash)
    
message = b'Ala ma kota'
md4_digest = MD4(message)
print(md4_digest)
