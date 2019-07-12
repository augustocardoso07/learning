n = int(input())

for _ in range(n):
    linha = input().split()
    linha.sort(key=len, reverse=True)
    print(*linha)