def foo(a, b):
    # CONDITIONALS
    if a > b:
        print a
    elif a < b:
        print b
    else:
        print a, b

    # WHILE LOOPS
    while (a < b):
        print a
        a += 1

if __name__ == "__main__":
    foo(10, 15)


