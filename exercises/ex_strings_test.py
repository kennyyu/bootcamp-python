import unittest
from ex_strings import *

class TestNumWords(unittest.TestCase):

    def test_empty(self):
        s = ""
        self.assertEqual(0, num_words(s))

    def test_one(self):
        s = "abc"
        self.assertEqual(1, num_words(s))

    def test_many(self):
        s = "a b c def gjijklj higj"
        self.assertEqual(6, num_words(s))

class TestSumList(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(0, sum_list([]))

    def test_one(self):
        self.assertEqual(-1, sum_list([-1]))

    def test_many(self):
        self.assertEqual(7, sum_list([-2, -3, 5, 8, 0, -1]))

class TestAppears(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(False, appears_in_list("foo", []))

    def test_positive(self):
        self.assertEqual(True, appears_in_list("f", ["a", "b", "f", "d"]))

    def test_negative(self):
        self.assertEqual(False, appears_in_list("f", ["a", "b", "c"]))

class TestReverse(unittest.TestCase):

    def test_empty(self):
        self.assertEqual([], reverse_list([]))

    def test_many(self):
        self.assertEqual(["a", "b", "c"], reverse_list(["c", "b", "a"]))

if __name__ == '__main__':
    unittest.main()
