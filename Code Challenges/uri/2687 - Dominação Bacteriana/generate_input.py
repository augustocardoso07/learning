import random
print(100)
l =[0, 1]

def linha():
    return [random.choice(l), random.choice(l), random.choice(l)]

for _ in range(100):
    print(3)
    print(*linha())
    print(*linha())
    print(*linha())
