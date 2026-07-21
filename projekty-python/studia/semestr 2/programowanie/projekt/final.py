import struct

def F(x, y, z):
    return (x & y) | ((~x) & z)

def G(x, y, z):
    return (x & y) | (x & z) | (y & z)

def H(x, y, z):
    return x ^ y ^ z

def round_constants():
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

    return round_constants

def md4(message):
    message = bytearray(message, 'utf-8')
    length = struct.pack('<Q', 8 * len(message))
    message.append(0x80)
    while (len(message) % 64) != 56:
        message.append(0)
    message += length

    a = 0x67452301
    b = 0xefcdab89
    c = 0x98badcfe
    d = 0x10325476

    round_const = round_constants()

    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        a_temp = a
        b_temp = b
        c_temp = c
        d_temp = d

        for j in range(16):
            if j < 12:
                if round_const[j][0] == "F":
                    f = F(b_temp, c_temp, d_temp)
                elif round_const[j][0] == "G":
                    f = G(b_temp, c_temp, d_temp)
                elif round_const[j][0] == "H":
                    f = H(b_temp, c_temp, d_temp)
                index = round_const[j][1]
                shift = round_const[j][2]
                k = round_const[j][3]
            else:
                if round_const[j][0] == "F":
                    f = F(b_temp, c_temp, d_temp)
                elif round_const[j][0] == "G":
                    f = G(b_temp, c_temp, d_temp)
                elif round_const[j][0] == "H":
                    f = H(b_temp, c_temp, d_temp)
                index = (round_const[j][1] + 4*j // 16) % 16
                shift = round_const[j][2]
                k = round_const[j][3]

            temp = (a_temp + f + struct.unpack("<I", chunk[index*4:index*4+4])[0])
            temp = (temp << shift) | (temp >> (32 - shift))
            temp = temp & 0xffffffff

            if round_const[j][0] == "F":
                a_temp = d_temp
                d_temp = c_temp
                c_temp = b_temp
                b_temp = temp
            elif round_const[j][0] == "G":
                a_temp = d_temp
                d_temp = c_temp
                c_temp = b_temp
                b_temp = temp
            elif round_const[j][0] == "H":
                a_temp = d_temp
                d_temp = c_temp
                c_temp = b_temp
                b_temp = temp

        a = (a + a_temp) & 0xffffffff
        b = (b + b_temp) & 0xffffffff
        c = (c + c_temp) & 0xffffffff
        d = (d + d_temp) & 0xffffffff

    result = struct.pack("<4I", a, b, c, d)
    return result.hex()

message = "Ala ma kota"
hash_value = md4(message)
print(hash_value)
