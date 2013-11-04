#!/usr/bin/env python

import dictionary
import sys
import time

if len(sys.argv) < 3:
    print "usage: %s dictionary-file text-file" % sys.argv[0]
    sys.exit(-1)

dictionary_name = sys.argv[1]
text_file_name = sys.argv[2]

start = time.clock()

dict = dictionary.load(dictionary_name)
print "dictionary size: %d" % dictionary.size(dict)

text_file = open(text_file_name, "rb")
num_misspelled = 0
for word in text_file:
    if not dictionary.check(dict, word):
        num_misspelled += 1
text_file.close()

print "num misspelled: %d" % num_misspelled
dictionary.unload(dict)

stop = time.clock()
print "time (s):", stop - start

