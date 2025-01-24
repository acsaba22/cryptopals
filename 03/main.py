from dataclasses import dataclass
from typing import Optional
import pprint
import string

def xorRepeat(buf: bytes, c: int) -> bytes:
    ret = bytearray(len(buf))
    for i, v in enumerate(buf):
        ret[i] = v ^ c
    return bytes(ret)

def countLetters(buf: bytes) -> int:
    ret = 0
    for v in buf:
        if ord('A') <= v and v <= ord('Z'):
            ret += 1
        elif ord('a') <= v and v <= ord('z'):
            ret += 1
        elif v == ord(' '):
            ret += 1
    return ret

@dataclass(order=True)
class ScoredGuess:
    score: float = float('-inf')
    key: Optional[int] = None
    chiperText: Optional[bytes] = None
    plainText: Optional[bytes] = None

    @classmethod
    def FromKey(cls, chiperText: bytes, key_: int):
        plainText = xorRepeat(chiperText, key_)
        score = countLetters(plainText)
        return cls(score, key_, chiperText, plainText)

def crackXorCipherSimple(chiper: bytes) -> ScoredGuess:
    bestGuess = ScoredGuess()
    for i in range(256):
        bestGuess = max(bestGuess, ScoredGuess.FromKey(chiper, i))

    return bestGuess

def crackXorCipher(chiper: bytes) -> ScoredGuess:
    bestGuess = ScoredGuess()
    counts = {v: chiper.count(v) for v in chiper}

    goodChars = string.ascii_letters + ' '
    for i in range(256):
        score = 0
        for c in goodChars:
            score += counts.get(ord(c)^i, 0)
        bestGuess = max(bestGuess, ScoredGuess(score, i))

    bestGuess.chiperText = chiper
    bestGuess.plainText = xorRepeat(chiper, bestGuess.key)
    return bestGuess


if __name__ == "__main__":
    chiper = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print(f'{chiper=}')
    pprint.pprint(crackXorCipherSimple(chiper))
    pprint.pprint(crackXorCipher(chiper))
