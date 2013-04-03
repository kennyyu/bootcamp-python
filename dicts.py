# See http://docs.python.org/2/tutorial/datastructures.html#dictionaries
# for more information
def foo():
    d = {} # declare a dictionary
    # a dictionary can take any object and map it to any other object
    d["c"] = 5
    d[6] = "foo"
    d["charmander"] = "pokemon"
    d[9] = "cake"

    print d
    print d["c"]

    # loop over a dictionary
    for key in d:
        print key, "=>", d[key]

if __name__ == "__main__":
    foo()

