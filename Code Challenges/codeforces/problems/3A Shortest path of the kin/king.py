from queue import Queue

offset = (# l   c
    ( "L",  0, -1),
    ( "R",  0,  1),
    ( "U",  1,  0),
    ( "D", -1,  0),

    ("LU",  1, -1),
    ("LD", -1, -1),
    ("RU",  1,  1),
    ("RD", -1,  1)
)


def possible(i, j):
    return 0 <= i < 8 and 0 <= j < 8


def bfs(s, t):

    queue = Queue()
    s = (int(s[1]) - 1, ord(s[0]) - 97, [])
    ti, tj = (int(t[1]) - 1, ord(t[0]) - 97)
    queue.put(s)

    visited = [[False] * 8 for _ in range(8)]

    while True:
        i, j, path = queue.get()
        if i == ti and j == tj: return len(path), path
        visited[i][j] = True

        for direction, di, dj in offset:
            newi = i + di
            newj = j + dj
            if possible(newi, newj) and not visited[newi][newj]:
                queue.put((newi, newj, path + [direction]))



def main():
    s = input()
    t = input()

    n, path = bfs(s, t)
    print(n)
    print(*path, sep="\n")


if __name__ == '__main__':
    main()