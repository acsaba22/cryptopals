
def HexToBinary(s):
    ret = []
    if len(s) % 2 != 0:
        raise Exception('Hex string should have even number: ' + len(s))
    v = 0
    bit = 0
    for (i, char) in enumerate(s):
        if '0' <= char and char <= '9':
            v += ord(char) - ord('0')
        elif 'a' <= char and char <= 'f':
            v += ord(char) - ord('a') + 10
        else:
            raise Exception('Unkown character in hex: |' + char + '|');
        if i%2 == 0:
            v <<= 4
        else:
            ret.append(v)
            v = 0
    return bytearray(ret)

def _ConstructBase64Map():
    ret = []
    for c in range(ord('A'),ord('Z')+1):
        ret.append(chr(c))
    for c in range(ord('a'),ord('z')+1):
        ret.append(chr(c))
    for c in range(ord('0'),ord('9')+1):
        ret.append(chr(c))
    ret.append('+')
    ret.append('/')
    return ret

_base64Map = _ConstructBase64Map()

def BinaryToBase64(binary):
    # global _base64Map
    v = 0
    bits = 0
    ret = ''

    def printIfCan():
        nonlocal v, bits, ret
        global _base64Map
        if bits < 6:
            return
        v2 = v >> (bits - 6)
        ret += _base64Map[v2]
        v2 <<= (bits - 6)
        v &= ~v2
        bits -= 6

    for x in binary:
        v <<= 8
        v += x
        bits += 8
        printIfCan()
        printIfCan()

    if bits != 0:
        v <<= 6 - bits
        bits = 6
        printIfCan()
    return ret

def HexToBase64(s):
    return BinaryToBase64(HexToBinary(s))

exampleHex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expectedExmpleBase64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def main():
    print("Example hex: " + exampleHex)
    print("decoded bytes: " + str(HexToBinary(exampleHex)))
    print("Base64: " + BinaryToBase64(HexToBinary(exampleHex)))


if __name__ == "__main__":
    main()
