from max_heap import build_max_heap
from min_heap import build_min_heap
import unittest

A = [3,5,7,8,1,4,2,45,32]

class Test(unittest.TestCase):
    def test_max(self):
        self.assertEqual(build_max_heap(A), [45, 32, 7, 8, 1, 4, 2, 3, 5])

    def test_min(self):
        self.assertEqual(build_min_heap(A), [1, 3, 2, 5, 32, 4, 7, 8, 45])


if __name__ == '__main__':
    unittest.main()