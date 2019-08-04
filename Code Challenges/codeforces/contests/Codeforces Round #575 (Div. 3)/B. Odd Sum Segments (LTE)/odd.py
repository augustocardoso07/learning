from sys import stdin
input = stdin.readline

q = int(input())

for _ in range(q):
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]

    only_odds = [(i, x) for i, x in enumerate(array, 1) if x % 2 != 0]

    l = len(only_odds)
    if l >= k and l % 2 == k % 2:
        result = [i for i, v in only_odds[:k]]
        result.pop()
        result.append(n)

        print("YES")
        print(*result)
    else:
        print("NO")