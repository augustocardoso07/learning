n, m = [int(x) for x in input().split()]
s = set()
for _ in range(m):
    t, a, b = [int(x) for x in input().split()]
    if t == 0:
        if (a, b) in s: print(1)
        else: print(0)
    else:
        s.add((a, b))
        s.add((b, a))