from c02 import main
import unittest

class Test_TestHexXor(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            main.XorBytes(
                '1c0111001f010100061a024b53535009181c',
                '686974207468652062756c6c277320657965'),
            b'746865206b696420646f6e277420706c6179')


if __name__ == '__main__':
    unittest.main()
