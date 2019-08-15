from queue import Queue
from datetime import datetime


def bfs(a, b):
    result = 0
    q = Queue()
    s = {a}
    q.put((a, 0))

    while a != b:
        a, result = q.get()
        temp = a + 1
        if not temp in s:
            if temp == b: return result + 1
            q.put((temp, result + 1))
            s.add(temp)
        temp = int(str(a)[::-1])
        if not temp in s:
            if temp == b: return result + 1
            q.put((temp, result + 1))
            s.add(temp)
        #print(a)

    return result


n = int(input())

inicial = datetime.now()
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    result = bfs(a, b)
    print(result)
print(datetime.now() - inicial)