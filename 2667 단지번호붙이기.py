import sys
from collections import deque
input = sys.stdin.readline
d = []
dd = [[0,1],[0,-1],[1,0],[-1,0]]
queue = deque()
graph = []
result = 0
def canGo(r,c,graph):
    return 0<=r<= len(graph)-1 and 0<=c<= len(graph[0])-1
def dfs(r,c,graph):
 global count
 for dr,dc in dd:
        ddr = dr+r
        ddc = dc+c
        if canGo(ddr,ddc,graph) and graph[ddr][ddc] == 1:
            graph[ddr][ddc] = 0
            count +=1
            dfs(ddr,ddc,graph)

for i in range(int(input())):
    c = list(map(int,input().rstrip()))
    graph.append(c)
    for k in range(len(c)):
        if c[k] == 1:
            queue.append([i,k])
while queue:
    r,c = queue.popleft()
    if graph[r][c] == 1:
        result+=1
        graph[r][c] = 0
        count =1
        dfs(r,c,graph)

    else:
        continue    
    d.append(count)
d.sort()
print(result)
for i in d:
    print(i)

        