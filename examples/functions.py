# To declare a function, use the `def` keyword,
# followed by the function name, and then arguments
# in parentheses.
def add(x, y):
    return x + y

print "add(5,4)", add(5,4)
print "add(3,6)", add(3,6)

# A function does not need to return anything. In this
# case, the special value None will be the return value.
#
# A function can also have default values for arguments
# if those values are not provided when the function
# is called.
def repeat(s, prefix="Hi", n=5):
    for i in range(n):
        print i, prefix, s

repeat("cat", "Hello", 3)        # prefix == "Hello", n == 3
repeat("cat", prefix="Bye")      # prefix == "Bye", n == 5
repeat("dog", prefix="Hi", n=3)  # prefix == "Hi", n == 3
repeat("food")                   # prefix == "Hi", n == 5

def sum_range(low, high):
    """
    This will sum up all the integers in the half-open
    interval [low, high).

    Triple quotes are special comments that you can place
    inside a function. These comments serve as the
    documentation string for this function (what you
    see when type help(function_name) at the top level.
    """
    # range(low, high) will generate a sequence of all the
    # integers in the range [low, high)
    #
    # sum is a built-in function that will sum all the numbers
    # in a given sequence.
    return sum(range(low, high))

print "sum_range(10,20)", sum_range(10, 20)
