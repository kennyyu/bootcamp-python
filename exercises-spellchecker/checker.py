#!/usr/bin/env python

import dictionary
import sys
import time

def sanitize_word(word):
    """
    1. Transforms the word to lower case
    2. Removes any surrounding whitespace
    3. Removes any leading or trailing punctuation
    """
    word = word.lower()
    word = word.strip()
    punct = set("[]*()-,.:;?!/`\"\'")
    should_delete = True
    while should_delete:
        if len(word) == 0:
            break
        should_delete = False
        if len(word) > 0 and word[-1] in punct:
            word = word[:-1]
            should_delete = True
        if len(word) > 0 and word[0] in punct:
            word = word[1:]
            should_delete = True
        word = word.strip()
    return word

if len(sys.argv) < 3:
    print "usage: %s dictionary-file text-file" % sys.argv[0]
    sys.exit(-1)

dictionary_name = sys.argv[1]
text_file_name = sys.argv[2]

start = time.clock()

dict = dictionary.load(dictionary_name)
text_file = open(text_file_name, "rb")
misspelled = set()
num_total = 0
for line in text_file:
    line = line.replace("-", " ")
    for word in line.split():
        word = sanitize_word(word)
        if len(word) == 0:
            continue
        if not dictionary.check(dict, word):
            num_total += 1
            misspelled.add(word)
text_file.close()

print misspelled
print "dictionary size: %d" % dictionary.size(dict)
print "num misspelled: %d" % num_total
print "num unique: %d" % len(misspelled)

dictionary.unload(dict)

stop = time.clock()
print "time (s):", stop - start

