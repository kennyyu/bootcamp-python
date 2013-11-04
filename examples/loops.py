# Example of a while loop.
# This computes the sum of the integers 0 + 1 + ... + 99
# and stores the result in the variable `s`
n = 0
s = 0
while n < 100:
    s += n
    n += 1
print "s:", s

# This is an example of a for loop.
# This allows us to iterate over all the items in a collection.
# The variable `item` will take on all the values in `lst`, one per iteration.
lst = ["apple", "bar", "orange"]
for item in lst:
    print item

# range() is a function that allows us to generate a sequence
# of integers in a certain range. range(100) will generate the sequence:
# 0, 1, 2, ... 99
#
# To see the documentation for range(), open up the python top-level and type:
#
#    help(range)
s2 = 0
for n in range(100):
    s2 += n
print "s2:", s
