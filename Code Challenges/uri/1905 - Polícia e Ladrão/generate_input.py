import random

print(400)

l = [0, 1]

def linha():
    return [random.choice(l) for _ in range(5)]

for i in range(400):
    print()
    for _ in range(5):
        print(*linha())