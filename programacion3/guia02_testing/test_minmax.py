import unittest
from minmax import min_max

class TestMinMax(unittest.TestCase):
    def test_uno(self):
        self.assertTrue(min_max([1]) == (1,1))
    def test_dos(self):
        self.assertTrue(min_max([1,30,100])==(1,100))
if __name__ == '__main__':
    unittest.main()