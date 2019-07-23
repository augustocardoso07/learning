import math

# def coutBits(n):
#     n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
#     n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
#     n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
#     n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
#     n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
#     n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32)  # This last & isn't strictly necessary.
#     return n


def bitcount(n):
    count = 0
    while n > 0:
        if (n & 1 == 1): count += 1
        n >>= 1

    return count

t = int(input())

for _ in range(t):
    n = int(input())

    conjuntos = []
    for i in range(n):
        rest = [int(x) for x in input().split()][1:]
        value = 0
        for v in rest:
            value |= (1 << v)
        conjuntos.append(value)

    q = int(input())

    for _ in range(q):
        p, a, b = [int(x) - 1 for x in input().split()]
        result = conjuntos[a] & conjuntos[b] if p == 0 else conjuntos[a] | conjuntos[b]
        print(bitcount(result))
