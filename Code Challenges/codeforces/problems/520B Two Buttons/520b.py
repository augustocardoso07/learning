from queue import Queue


def bfs(n, m):

    q = Queue()

    q.put((n, 0))

    visited = {n}

    while not q.empty():
        value, moves = q.get()
        if value == m: return moves

        for v in [value * 2, value - 1]:
            if v not in visited and 0 <= v <= 80000:
                visited.add(v)
                q.put((v, moves + 1))

    return "NO"


def main():
    n, m = [int(x) for x in input().split()]
    result = bfs(n, m)
    print(result)


if __name__ == '__main__':
    main()
