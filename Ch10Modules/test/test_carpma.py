import unittest
from dort_islem.carpma import carp

class TestCarpma(unittest.TestCase):
    def test_carp(self):
        self.assertEqual(carp(5, 3), 15)
        self.assertEqual(carp(1, 0), 0)
        self.assertEqual(carp(-1, 1), -1)

if __name__ == '__main__':
    unittest.main()
