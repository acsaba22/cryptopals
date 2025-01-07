import base64

def XorBytes(hex1, hex2):
    if len(hex1) != len(hex2):
        raise Exception('Lengths should be the same')
    b1 = base64.b16decode(hex1, casefold=True)
    b2 = base64.b16decode(hex2, casefold=True);

    ret = bytearray(len(b1))
    for i, v1 in enumerate(b1):
        ret[i] = v1 ^ b2[i]
    return base64.b16encode(ret).lower()


