def foo():
    s = "foood cake cheese"
    print len(s)

    # split string by spaces, return list of words
    words = s.split()
    print words
    print len(words)

    # keyfunc and keyfunc2 are exactly the same
    # lambdas are just syntactic sugar
    keyfunc = lambda word : len(word)

    def keyfunc2(word):
        return len(word)

    # sort words by length of the word
    # functions can take *named* arguments, e.g. you can specify
    # parameters on a function that are optional (like key)
    # if you choose to provide them you call it like so:
    words_sorted = sorted(words, key=keyfunc)
    print words_sorted

if __name__ == "__main__":
    foo()
