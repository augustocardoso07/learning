from random import randint
n = 1000
print(n)
for i in range(n):
    m = randint(1, n)
    files = []
    for j in range(m):
        file = randint(1, n)
        while file == i + 1:
            file = randint(1, n)
        files.append(file)
    line = [m] + files
    print(*line)