import sys
sys.setrecursionlimit(500**2)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def outLines(r, c):
    return 0 <= r < n and 0 <= c < m

visited = [[-1] * m for _ in range(n)]

def dfs(r, c):
    if r == n - 1 and c == m - 1:
        return 1

    if visited[r][c] != -1:
        return visited[r][c]

    visited[r][c] = 0
    for dr, dc in dd:
        ddr, ddc = dr + r, dc + c
        if outLines(ddr, ddc) and graph[r][c] > graph[ddr][ddc]:
            visited[r][c] += dfs(ddr, ddc)

    return visited[r][c]
print(visited)
count = dfs(0, 0)
print(count)