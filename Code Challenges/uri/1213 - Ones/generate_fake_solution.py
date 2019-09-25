from uri1213 import solve

for i in range(1, 10001):
    if not (i % 2 == 0 or i % 5 == 0):
        print("{}: {},".format(i, solve(i)))