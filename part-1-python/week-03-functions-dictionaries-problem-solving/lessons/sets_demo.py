a = [3, 1, 3, 2, 1]
s = set(a)
print(s, len(s))
print(2 in s, 5 in s)

t = {2, 3, 4}
print(s & t, s | t, s - t)

e = {}
print(type(e))