q = int(input())

for _ in range(q):
    alice, bob, c = sorted([int(x) for x in input().split()])
    c -= bob - alice
    alice += (bob - alice)
    alice += c // 2
    print(alice)
