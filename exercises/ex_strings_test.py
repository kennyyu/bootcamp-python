import unittest
import ex_strings

class TestNumWords(unittest.TestCase):

    def test_empty(self):
        s = ""
        self.assertEqual(0, ex_strings.num_words(s))

    def test_one(self):
        s = "abc"
        self.assertEqual(1, ex_strings.num_words(s))

    def test_many(self):
        s = "a b c def gjijklj higj"
        self.assertEqual(6, ex_strings.num_words(s))

if __name__ == '__main__':
    unittest.main()
