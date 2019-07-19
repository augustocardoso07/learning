area_externa = 0
offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def possible(m, i, j, l):
    return not (i < 0 or j < 0 or i >= l or j >= l or m[i][j] == "!" or m[i][j] == 1)

def dfs(m, i, j, l):
    if m[i][j] == 1: return
    if m[i][j] == 0:
        global area_externa
        area_externa += 1
        m[i][j] = "!"
    # print("novo movimento")
    # [print(line) for line in m]

    for direction in offset:
        new_i = i + direction[0]
        new_j = j + direction[1]
        p = possible(m, new_i, new_j, l)
        if p:
            dfs(m, new_i, new_j, l)

def solve(m, l):
    for i in (0, l - 1):
        for j in range(l):
            dfs(m, i, j, l)

    for i in range(l):
        for j in (0, l - 1):
            dfs(m, i, j, l)

    return "{:.2f}".format((l * l - area_externa) / 2)

def main():
    n = int(input())
    for _ in range(n):
        l = int(input())
        m = []
        global area_externa
        area_externa = 0
        for _ in range(l):
            line = [int(x) for x in input().split()]
            m.append(line)
        # print("-------------- novo jogo")
        print(solve(m, l))

if __name__ == "__main__":
    main()