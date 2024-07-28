import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

queue = deque()

n,m,k = map(int,input().split())

graph = [[0] * m for _ in range(n)]

tf = [[False] * m for _ in range(n)]

for iw in range(n):
    for kw in range(m):
        queue.append([iw,kw])

for _ in range(k):
    fx,fy,ffx,ffy = map(int,input().split())
    for qq in range(fy,ffy):
        for ww in range(fx,ffx):
            graph[qq][ww] = 1

dd = [[0,1],[0,-1],[1,0],[-1,0]]

def outLines(r,c):
    return 0 <= r < n and 0 <= c < m

def dfs(r,c,graph):
    global counted 
    for dr,dc in dd:
        ddr = dr+r
        ddc = dc + c
        if outLines(ddr,ddc) and not tf[ddr][ddc] and  graph[ddr][ddc] == 0:
            tf[ddr][ddc] = True
            counted +=1
            dfs(ddr,ddc,graph)
ff = []
result = 0

counted = 0

while queue:
 r,c = queue.popleft()
 if tf[r][c] or graph[r][c] == 1:
     continue
 counted +=1
 tf[r][c] = True
 dfs(r,c,graph) 
 ff.append(counted)
 result +=1
 counted = 0

ff.sort()
print(result)
for x in ff:
    print(x, end = " ")






