import unittest
from dort_islem.bolme import bol

class TestBolme(unittest.TestCase):
    def test_bol(self):
        self.assertEqual(bol(6, 3), 2)
        self.assertEqual(bol(1, 1), 1)
        self.assertRaises(ValueError, bol, 1, 0)

if __name__ == '__main__':
    unittest.main()
