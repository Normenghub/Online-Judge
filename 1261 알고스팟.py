import sys
from collections import deque
input = sys.stdin.readline
q = deque()

n,m = map(int,input().split())

graph = []
q.append((0,0))

def outLines(r,c):
    return 0<= r < m and 0 <= c < n

dd = [[0,1],[0,-1],[1,0],[-1,0]]
INF = 10e8
visited = [[INF] * n for _ in range(m)]
visited[0][0] = 0

for _ in range(m):
    arr = list(input().rstrip())
    x = []
    for i in arr:
        x.append(int(i))
    graph.append(x)

while q:
    r,c = q.popleft()
    for dr,dc in dd:
        ddr,ddc = dr+r,dc+c
        if outLines(ddr,ddc) and graph[ddr][ddc] == 0:
            if visited[ddr][ddc] > visited[r][c]:
                visited[ddr][ddc] = visited[r][c]
                q.append([ddr,ddc])
        elif outLines(ddr,ddc) and graph[ddr][ddc] == 1:
            if visited[ddr][ddc] > visited[r][c] + 1:
                visited[ddr][ddc] = visited[r][c] + 1
                q.append([ddr,ddc])
print(visited[m-1][n-1])
            