s = set([5, 6, 7, 5, 6, 7, 1, 5, 6, 7])
print s
print "length", len(s)

for item in s:
    print item

print "is 4 in set", 4 in s
s.add(4)
print "is 4 in set", 4 in s

print "sum", sum(s)
