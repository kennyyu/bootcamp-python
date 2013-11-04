# Declare a list of strings
l = ["food", "cat", "bar"]
print l
print len(l) # print the length of the list
print l[1] # print "cat"

# append to the end of the list
l.append("dog")
l[2] = "homer" # replace "bar" with "homer"
print l
print len(l)

# Traverse the list
for s in l:
    print s

# Slicing a list
m = list(range(20))
print "m", m
print "m[-1]", m[-1] # last element
print "m[10:]", m[10:] # print the rest of list starting starting at index 10
print "m[:10]", m[:10] # print from the beginning of the list up to but not includinx index 10
print "m[5:15]", m[5:15] # print starting from 5 and up to but not including 15
print "m[5:-2:3]", m[5:-2:3] # print every 3rd element, starting at index 5 and going up-to-but-not-including the second-to-last element

