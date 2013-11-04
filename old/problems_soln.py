# PROBLEM: Write a function to return the sum of a list of numbers:
# HINT: there is a built in sum function
def my_sum(lst):
    s = 0
    for n in lst:
        s += n
    return s

print "my_sum", my_sum([1, 2, 3, 4])

def my_sum_better(lst):
    return sum(lst)

# PROBLEM: Write a function that returns a list of words in a string sorted by
# the length of a word.
def size_order(s):
    words = s.split()
    word_set = set(words) # generate a set of of these words to eliminate dups
    return sorted(word_set, key=lambda word: len(word))

print "size_order", size_order("a aa aaaaaa aaa aaaaaaaaaa")

# PROBLEM: Write a function that returns the character that appears
# most frequently in a string s
def most_frequent(s):
    # Create a mapping from char => count
    count = {}
    for c in s: # loop over characters
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    # Sort dictionary keys by values, return in descending order
    # key is a function that tells us how to compare something in our
    # collection count
    sorted_count = sorted(count, key=count.get, reverse=True)

    # first item would have the largest count
    return sorted_count[0]

print "most_frequent", most_frequent("foooooood")
print "most_frequent", most_frequent("aaabbbb")

# PROBLEM: Write a function that counts the number of words in a string.
# e.g. "this is food" ==> 3
def num_words(s):
    words = s.split()
    return len(words)

print "num_words", num_words("this is food")

# PROBLEM: Write a function that returns a list of words that appear
# more than n times in a string
def frequent_words(s, n):
    words = s.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    # filter and keep words whose count is > n
    return filter(lambda word: count[word] > n, count.keys())

print "frequent_words", frequent_words("aa aa aa aa bb bb bb bb bb food food", 3)
