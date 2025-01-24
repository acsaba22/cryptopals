from c04 import main
import unittest

class Test_TestHexXor(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            main.FindEncrypted(),
            b'Now that the party is jumping\n')


if __name__ == '__main__':
    unittest.main()
