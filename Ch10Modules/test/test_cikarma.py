import unittest
from dort_islem.cikarma import cikar

class TestCikarma(unittest.TestCase):
    def test_cikar(self):
        self.assertEqual(cikar(5, 3), 2)
        self.assertEqual(cikar(1, 1), 0)
        self.assertEqual(cikar(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
