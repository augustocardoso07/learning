n, m = [int(x) for x in input().split()]

result = 0
for _ in range(n):
    floor = [int(x) for x in input().split()]
    for i in range(0, 2 * m, 2):
        result += (floor[i] | floor[i + 1])

print(result)