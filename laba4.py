a = 1
b = 2

a, b = b, a
print(a, b)

c = 3
d = 4

buf = c
c = d
d = buf
print(c, d)