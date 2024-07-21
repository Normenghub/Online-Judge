import sys
copyGraph = []
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
maps = deque()
asd = []
graph = []
for i in range(n):
    x = list(input().rstrip())
    for k in range(m):
        if x[k] == 'L':
            maps.append([i,k])
    graph.append(x)

maxs = 0

dd = [[0,1],[0,-1],[1,0],[-1,0]]

def canGo(r,c):
    return 0 <= r < n and 0 <= c < m


def bfs(graph,x,y):
    global maxs, asd
    o = deque()
    graph[x][y] = 0

    o.append([x,y])

    while o:
        q , w = o.popleft()
        asd.append([q,w])
        for dx,dy in dd:
         ddx = dx + q 
         ddy = dy + w
         if canGo(ddx,ddy) and graph[ddx][ddy] == 'L':
             graph[ddx][ddy] = graph[q][w] +1
             maxs = max(maxs, graph[ddx][ddy])
             o.append([ddx,ddy])
             asd.append([ddx,ddy])
    

while maps:
    a,b = maps.popleft()

    bfs(graph,a,b)
    for x, y in asd:
        graph[x][y]= 'L'
    asd= []


print(maxs)

