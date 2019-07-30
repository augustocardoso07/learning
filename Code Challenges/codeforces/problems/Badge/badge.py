def dfs(i, students):
    visited = [False] * n

    while not visited[i]:
        visited[i] = True
        i = students[i]

    return i + 1


n = int(input())
students = [int(x) - 1 for x in input().split()]

result = [dfs(i, students) for i in range(n)]
print(*result)