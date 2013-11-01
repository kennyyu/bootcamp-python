def num_words(s):
    words = s.split()
    return len(words)

def sum_list(lst):
    return sum(lst)

def appears_in_list(x, lst):
    return x in lst

def num_unique(lst):
    return len(set(lst))

def reverse_list(lst):
    return list(reversed(lst))

def sort_reverse(lst):
    return sorted(lst, reverse=True)

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        s = s.replace(vowel, "")
    return s

def longest_word(lst):
    if len(lst) == 0:
        return None
    sort_by_length = sorted(lst, key=len, reverse=True)
    return sort_by_length[0]

def word_frequency(lst):
    freq = {}
    for word in lst:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    return freq

def most_frequent_word(lst):
    if len(lst) == 0:
        return None
    freq = word_frequency(lst)
    sort_by_freq = sorted(freq.items(), key=lambda (word,count): count, reverse=True)
    return sort_by_freq[0]

def find_mismatch(lst1, lst2):
    mismatch = []
    for (word1, word2) in zip(lst1, lst2):
        if word1 != word2:
            mismatch.append((word1, word2))
    return mismatch

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
