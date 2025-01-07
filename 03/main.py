
def xorRepeat(buf: bytearray, c: int) -> bytearray:
    ret = bytearray(len(buf))
    for i, v in enumerate(buf):
        ret[i] = v ^ c
    return ret

def countLetters(buf: bytearray) -> int:
    ret = 0
    for v in buf:
        if ord('A') <= v and v <= ord('Z'):
            ret += 1
        elif ord('a') <= v and v <= ord('z'):
            ret += 1
    return ret


def findKey(chiper: bytearray) -> tuple[int, bytearray]:
    bestScore = 0
    bestText = bytearray()
    bestKey = 0
    for i in range(256):
        text = xorRepeat(chiper, i)
        score = countLetters(text)
        # print(f'{i} -> {score=}')
        if bestScore < score:
            bestScore = score
            bestText = text
            bestKey = i

    return bestKey, bestText

if __name__ == "__main__":
    chiper = bytearray.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print(f'{chiper=}')
    print(findKey(chiper))
