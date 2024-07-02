import sys
from collections import deque
input = sys.stdin.readline
graph = []
dd = [[0,1],[0,-1],[1,0],[-1,0]]
n,m=map(int,input().split())

def canGo(r,c):
    return 0<= r<=n-1 and 0<= c<=m-1
for _ in range(n):
    c = list(map(int,input().rstrip()))
    graph.append(c)
queue = deque([[0,0]])
while queue:
    v = queue.popleft()
    for dr,dc in dd:
        ddr=dr+v[0]
        ddc=dc+v[1]
        if canGo(ddr,ddc) and graph[ddr][ddc] == 1:
            graph[ddr][ddc] = graph[v[0]][v[1]] + 1
            queue.append([ddr,ddc])
print(graph[n-1][m-1])