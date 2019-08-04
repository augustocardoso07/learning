import random

print(1024, 1024)


def linha():
    l = [".", "o"]
    l = [random.choice(l) for _ in range(1024)]
    return "".join(l)


for i in range(1024):
    print(linha())
