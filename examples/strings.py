s = "foood cake cheese"
# print out the length of the string
# len() is a builtin.
print len(s)

# split string by spaces, return list of words
words = s.split()
print words
print len(words)

# keyfunc and keyfunc2 are exactly the same
# lambdas are just syntactic sugar to allow you
# to declare one-liner functions.
keyfunc = lambda word : len(word)

def keyfunc2(word):
    return len(word)

# sort words by length of the word
# The "key" argument of sorted tells us how to sort the list.
#
# Example:
# For the list: ["a", "aaa", "aa"],
# keyfunc will be appled on all the elements: [1, 3, 2]
# and then sorted: [1, 2, 3]
# and then replaced with their original entries: ["a", "aa", "aaa"]
words_sorted = sorted(words, key=keyfunc)
print words_sorted

# What else can you call on s?
# (i.e. for what `foo` can we do `s.foo()`?)
# To see what methods you can call on a variable, open up the top
# level, then enter:
#
# s = "food"
# dir(s)
#
# This will dump a list of all the things you can call the variable with.
# E.g. "join" will be in that list if you called dir() on a string.
# This means that you call `s.join()`.
#
# To see what it does, you can call:
#
# help(s.join)
#
# At the top level to open the documentation for the join function.
