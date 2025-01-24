from c01 import main
import unittest

class Test_TestHexToBase64(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            main.HexToBase64(main.exampleHex),
            main.expectedExmpleBase64)


if __name__ == '__main__':
    unittest.main()
