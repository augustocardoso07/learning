import queue

def bfs(v, k, servidores, n):
    q = queue.Queue()
    q.put(v)
    visitados = set()
    cout = 0
    resp = 1
    while resp != n:
        if cout == k: return resp
        v = q.get()
        visitados.add(v)
        for u in servidores[v]:
            if u not in visitados:
                resp += 1
                q.put(u)
        cout += 1
    return -1

while True:
    try:
        n, k = [int(x) for x in input().split()]
    except:
        break

    servidores = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = [int(x) - 1 for x in input().split()]
        servidores[v].append(u)
        servidores[u].append(v)

    max_infecao = 0

    for v in range(n):
        # bfs retorna o numero de computadores infequitado com tamanho k
        # retorna -1 se o tamanho da arvore for menor que k
        m = bfs(v, k, servidores, n)
        if m > max_infecao:
            max_infecao = m

    resp = max_infecao if max_infecao != 0 else "Impossible revenge!"
    print(resp)