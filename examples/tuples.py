def gen_tuple(s):
    """
    Returns a tuple of (input, length of input)
    """
    return (s, len(s))

v = gen_tuple("foood")
print v
(s, n) = v
print s
print n
