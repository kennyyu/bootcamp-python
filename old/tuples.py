def foo():
    # tuples allow you to pass multiple things around as a single unit
    # e.g. no need to create a new struct or a class if all you want
    # is to pass around some light-weight values.
    x = (5, "c")
    y = (6, "d")
    z = (8, 9, "cake", "d")
    print x
    print y

    l = []
    l.append(x)
    l.append(y)
    print l

    for item in l:
        (u, v) = item
        print u, v

if __name__ == "__main__":
    foo()
