# PROB 1
# Return the number of words in the string s. Words are separated by spaces.
# e.g. num_words("abc def") == 2
def num_words(s):
    words = s.split()
    return len(words)

# PROB 2
# Return the sum of all the numbers in lst. If lst is empty, return 0.
def sum_list(lst):
    return sum(lst)

# PROB 3
# Return True if x is in lst, otherwise return False.
def appears_in_list(x, lst):
    return x in lst

# PROB 4
# Return the number of unique strings in lst.
# e.g. num_unique(["a", "b", "a", "c", "a"]) == 3
def num_unique(lst):
    return len(set(lst))

# PROB 5
# Return a new list, where the contents of the new list are lst in reverse order.
# e.g. reverse_list([3, 2, 1]) == [1, 2, 3]
def reverse_list(lst):
    return list(reversed(lst))

# PROB 6
# Return a new list containing the elements of lst in sorted decreasing order.
# e.g. sort_reverse([5, 7, 6, 8]) == [8, 7, 6, 5]
def sort_reverse(lst):
    return sorted(lst, reverse=True)

# PROB 7
# Return a new string containing the same contents of s, but with all the
# vowels (upper and lower case) removed. Vowels do not include 'y'
# e.g. remove_vowels("abcdeABCDE") == "bcdBCD"
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        s = s.replace(vowel, "")
    return s

# PROB 8
# Return the longest word in the lst. If the lst is empty, return None.
# e.g. longest_word(["a", "aaaaaa", "aaa", "aaaa"]) == "aaaaaa"
def longest_word(lst):
    if len(lst) == 0:
        return None
    sort_by_length = sorted(lst, key=len, reverse=True)
    return sort_by_length[0]

# PROB 9
# Return a dictionary, mapping each word to the number of times the word
# appears in lst.
# e.g. word_frequency(["a", "a", "aaa", "b", "b", "b"]) == {"a": 2, "aaa": 1, "b": 3}
def word_frequency(lst):
    freq = {}
    for word in lst:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    return freq

# PROB 10
# Return the tuple (word, count) for the word that appears the most frequently
# in the list, and the number of times the word appears. If the list is empty, return None.
# e.g. most_frequent_word(["a", "a", "aaa", "b", "b", "b"]) == ("b", 3)
def most_frequent_word(lst):
    if len(lst) == 0:
        return None
    freq = word_frequency(lst)
    sort_by_freq = sorted(freq.items(), key=lambda (word,count): count, reverse=True)
    return sort_by_freq[0]

# PROB 11
# Compares the two lists and finds all the positions that are mismatched in the list.
# Assume that len(lst1) == len(lst2). Return a list containing the indices of all the
# mismatched positions in the list.
# e.g. find_mismatch(["a", "b", "c", "d", "e"], ["f", "b", "c", "g", "e"]) == [0, 3]
def find_mismatch(lst1, lst2):
    assert(len(lst1) == len(lst2))
    mismatch = []
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            mismatch.append(i)
    return mismatch

# PROB 12
# Returns the list of words that are in word_list but not in vocab_list.
def spell_checker(vocab_list, word_list):
    vocab_set = set(vocab_list)
    misspelled = set()
    for word in word_list:
        if word not in vocab_list:
            misspelled.add(word)
    return misspelled

def spell_checker2(vocab_list, word_list):
    vocab_set = set(vocab_list)
    return [word for word in word_list if word not in vocab_set]
