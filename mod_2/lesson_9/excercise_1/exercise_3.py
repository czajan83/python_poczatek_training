from random import randint

b = []
for a in range(20):
    b.append(randint(0, 1))

c = []
for a in range(20):
    c.append(randint(0, 1))

d = [*b, *c]

print(b)
print(c)
print(d)
