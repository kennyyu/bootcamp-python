d = {"cat" : 2, "tiger": 0}
d["food"] = 5
d["cheese"] = 7
d["apple"] = "orange"
d[8] = "penguin"

print d
print len(d) # number of keys
for key in d:
    print key, d[key]

for key, value in d.items():
    print key, value

print "check if food is in d", "food" in d
del d["food"]
print "check if food is in d", "food" in d

