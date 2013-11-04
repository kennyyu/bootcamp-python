# True and False must be capitalized
# To make variables, just declare it and
# assign it a value. The spaces around the "=" are optional.
b = True
c = False
d = 4
e = "apple"

# Example of an if-else-if statement.
# To check if two quantities are equal, use "=="
if d == 3:
    print "d is 3"
elif d == 4:
    food = d + 7
    print "FOOD", food
elif d == 5:
    print "d is 5"
else:
    print "d is not 3 or 4 or 5"

# Use "==" for strings as well!
if e == "apple":
    print e
else:
    print "NOT APPLE"

# Use "and" and "or" to take the logical and/or of
# two boolean values.
# Note that an if statement does not need to have a
# matching "else".
if b and c:
    print "b and c are both True"

if b or c:
    print "at least one of b or c is True"
