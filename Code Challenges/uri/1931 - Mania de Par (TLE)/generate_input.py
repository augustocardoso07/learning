from random import randint

c = 10 ** 4
v = 50000

print(c, v)
for _ in range(v):
    print(randint(1, c), randint(1, c), randint(1, c))