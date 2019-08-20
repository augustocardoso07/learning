from queue import PriorityQueue


def solve(graph, in_degrees, n):
    pq = PriorityQueue()

    for v in range(n):
        if in_degrees[v] == 0:
            pq.put(v)

    visited = [False] * n
    total = 0
    result = []
    while not pq.empty():
        v = pq.get()
        visited[v] = True
        total += 1
        result.append(v + 1)

        for u in graph[v]:
            if not visited[u]:
                in_degrees[u]-= 1
                if in_degrees[u] == 0:
                    pq.put(u)

    return result if total == n else None


def main():
    n, m = [int(xx) for xx in input().split()]

    graph = [[] for _ in range(n)]
    in_degrees = [0] * n

    for _ in range(m):
        x, y = [int(xx) - 1 for xx in input().split()]
        graph[x].append(y)
        in_degrees[y] += 1

    result = solve(graph, in_degrees, n)

    if result:
        print(*result)
    else:
        print("Sandro fails.")

if __name__ == '__main__':
    main()


def test_all(capsys):
    import sys
    from glob import glob

    ins = sorted(glob("in*"))
    outs = sorted(glob("out*"))

    with capsys.disabled():
        print()
        print("Arquivos testados: ", ins, outs)

    assert len(ins) == len(outs)

    for i in range(len(ins)):
        pathin = ins[i]
        pathout = outs[i]
        sys.stdin = open(pathin)
        main()
        out, err = capsys.readouterr()
        expected = open(pathout).read()
        assert expected == out
        with capsys.disabled():
            print("Teste {} ok!".format(i + 1))

    sys.stdin = sys.__stdin__