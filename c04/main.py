import os

from c03 import main as main03

# TODO don't log when it's in test

def FindEncrypted():
    with open(os.path.join(os.getcwd(), 'c04/input.txt')) as file:
        bestCrack = main03.ScoredGuess()
        for line in file:
            chiper = bytes.fromhex(line)
            crack = main03.crackXorCipher(chiper)
            bestCrack = max(bestCrack, crack)
        print(bestCrack.plainText)
        print(bestCrack.chiperText.hex())
        return bestCrack.plainText
    return Nones


if __name__ == "__main__":
    FindEncrypted()
