n = int(input())

for _ in range(n):
    input()
    v, a = [int(x) for x in input().split()]
    s = set()
    for _ in range(a):
        v, u = sorted([int(x) for x in input().split()])
        s.add((v, u))
    print(len(s) * 2)