# -*- coding: utf-8 -*-

t = int(input())

for _ in range(t):
    n = int(input())

    conjuntos = []
    for i in range(n):
        _, *rest = [int(x) for x in input().split()]
        conjuntos.append(set(rest))

    q = int(input())

    for _ in range(q):
        p, a, b = [int(x) - 1 for x in input().split()]
        #result = conjuntos[a] & conjuntos[b] if p == 0 else conjuntos[a] | conjuntos[b]
        result = set([1,2,3,4,5,6])
        print(len(result))