# see http://docs.python.org/2/tutorial/datastructures.html#more-on-lists for
# more information
def foo():
    lst = [] # create an empty list
    lst.append(5) # add 5 to end of list
    lst.append(6)
    lst.append(7)
    lst.append(8)
    lst.append(9)
    print lst
    print lst[0] + lst[1]
    print sum(lst)
    print lst[1:4] # lst[1:n] returns the sublist lst[1], lst[2], ... lst[n-1]
    print lst[-1] # return last item

    # looping over a list
    for x in lst:
        print x

    # loop over a range (no more for (int i = 0; i < n; i++) { ... } business)
    for i in range(n):
        print i

# This is the pattern you should use when you have python files
# that are imported by other python files, but don't necessarily
# want the code to actually be executed
if __name__ == "__main__":
    # this means that this python file is being executed
    foo()


