n, m = [int(x) for x in input().split()]
status = [False] * (n + 1)
_, *acesas = [int(x) for x in input().split()]

for i in acesas:
    status[i] = True

result = 0
for i in range(1, n + 1):
    if sum(status) == 0:
        break
    _ , *ligada = [int(x) for x in input().split()]
    for j in ligada:
        status[j] = not status[j]
    result += 1

if i == result:
    print(-1)
else:
    print(result)