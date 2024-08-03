import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

way = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]

path = [[-1] * m for _ in range(n)]

def out_of_bounds(r, c):
    return 0 <= r < n and 0 <= c < m

def dfs(r, c, cnt):
    if path[r][c] != -1:  
        return path[r][c] == cnt

    if visited[r][c]:  
        return False

    visited[r][c] = True
    path[r][c] = cnt

    dr, dc = way[graph[r][c]]
    nr, nc = r + dr, c + dc

    if out_of_bounds(nr, nc):
        if dfs(nr, nc, cnt):
            return True

    path[r][c] = -1
    return False

cycle_count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, i * m + j): 
                cycle_count += 1

print(cycle_count)