import unittest
from dort_islem.toplama import topla

class TestToplama(unittest.TestCase):
    def test_topla(self):
        self.assertEqual(topla(5, 3), 8)
        self.assertEqual(topla(-1, 1), 0)
        self.assertEqual(topla(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
