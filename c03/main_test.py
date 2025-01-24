from c03 import main
import unittest

class Test_TestHexXor(unittest.TestCase):
    def test_example(self):
        chiper = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        self.assertEqual(
            main.crackXorCipher(chiper).plainText,
            b"Cooking MC's like a pound of bacon")


if __name__ == '__main__':
    unittest.main()
