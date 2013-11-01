import unittest
from ex_strings import *

class TestNumWords(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(0, num_words(""))

    def test_one(self):
        self.assertEqual(1, num_words("abc"))

    def test_many(self):
        self.assertEqual(6, num_words("a b c def gjijklj higj"))

class TestLongestWord(unittest.TestCase):

    def test_empty(self):
        self.assertIsNone(longest_word([]))

    def test_many(self):
        self.assertEqual("aaaaaaaaaa",
                         longest_word(["a", "aaaaa", "aaaaaaaaaa", "aa", "aaa"]))

class TestNumUnique(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(0, num_unique([]))

    def test_many(self):
        self.assertEqual(3, num_unique(["a", "a", "aa", "ab", "ab", "ab", "aa"]))

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

class TestRemoveVowels(unittest.TestCase):

    def test_empty(self):
        self.assertEqual("", remove_vowels(""))

    def test_lower(self):
        self.assertEqual("bcdfghjklmnpqrstvwxyz", remove_vowels("abcdefghijklmnopqrstuvwxyz"))

    def test_upper(self):
        self.assertEqual("BCDFGHJKLMNPQRSTVWXYZ", remove_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def test_mix(self):
        self.assertEqual("bBcC", remove_vowels("aAbBcCeE"))

class TestWordFrequency(unittest.TestCase):

    def test_empty(self):
        words = []
        self.assertEqual(0, len(word_frequency(words)))

    def test_many(self):
        words = "a a a b b c c c c c c d d d d e".split()
        freq = word_frequency(words)
        expected_freq = {"a": 3, "b": 2, "c": 6, "d": 4, "e": 1}
        self.assertDictEqual(expected_freq, freq)

class TestMostFrequentWord(unittest.TestCase):

    def test_none(self):
        self.assertIsNone(most_frequent_word([]))

    def test_most_frequent(self):
        self.assertEqual(("aa", 4),
                         most_frequent_word(["aa", "aa", "b", "bb", "aa", "c", "aa", "b"]))

class TestSpellChecker(unittest.TestCase):

    def test_no_vocab(self):
        vocab = []
        words = ["a", "b", "c"]
        miss = spell_checker(vocab, words)
        expected_miss = ["a", "b", "c"]
        self.assertItemsEqual(miss, expected_miss)

    def test_vocab(self):
        vocab = ["cat", "dog", "fox", "pig", "sheep", "elephant"]
        words = ["cat", "dogg", "foxx", "fox", "pigg", "s", "sheep", "ee"]
        miss = spell_checker(vocab, words)
        expected_miss = ["dogg", "foxx", "pigg", "s", "ee"]
        self.assertItemsEqual(miss, expected_miss)

class TestFindMismatch(unittest.TestCase):

    def test_empty(self):
        self.assertEqual([], find_mismatch([], []))

    def test_many(self):
        lst1 = ["a", "b", "c", "d", "e"]
        lst2 = ["f", "b", "c", "g", "e"]
        mismatch = find_mismatch(lst1, lst2)
        expected_mismatch = [("a", "f"), ("d", "g")]
        self.assertItemsEqual(mismatch, expected_mismatch)

if __name__ == '__main__':
    unittest.main()
