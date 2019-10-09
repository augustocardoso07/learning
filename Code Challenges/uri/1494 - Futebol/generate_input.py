from random import randint
n = 10
g = 10


for _ in range(50):
    print(n, g)
    for i in range(n):
        print(randint(0, 100), randint(0, 100))
