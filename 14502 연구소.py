import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

graph = []
countZero = 0
copyForCountZero = 0
n,m = map(int,input().split())
queue = deque()
zeroCoordinate = deque()
tf = []
queue2 = deque()
maxs = -1

for i in range(n):
    x = list(map(int,input().split()))
    for k in range(m):
        if x[k] == 2:
            queue2.append([i,k])
        elif x[k] == 0:
            zeroCoordinate.append([i,k])
            countZero +=1
    graph.append(x)
countZero -=3
permutationsOfbarrier = deque(combinations(zeroCoordinate,3))

dd = [[0,1],[0,-1],[1,0],[-1,0]]

def canGo(r,c):
    return 0<= r <n and 0<= c<m

def bfs(queue,tf,dd,copyForCountZero):
    while queue:
        a,b = queue.popleft()
        for dr,dc in dd:
            ddr = dr + a
            ddc = dc + b
            if canGo(ddr,ddc) and not tf[ddr][ddc] and graph[ddr][ddc] == 0:
                copyForCountZero -=1
                queue.append([ddr,ddc])
                tf[ddr][ddc] = True
    return copyForCountZero


    
while permutationsOfbarrier:
    a,b,c = permutationsOfbarrier.popleft()
    graph[a[0]][a[1]]=1
    graph[b[0]][b[1]]=1
    graph[c[0]][c[1]] =1
    tf = [[False] * m for _ in range(n)]
    queue = deque(queue2)
    asdf =bfs(queue,tf,dd,copyForCountZero)
    maxs = max(maxs,asdf)
    copyForCountZero = countZero
    graph[a[0]][a[1]]=0
    graph[b[0]][b[1]]=0
    graph[c[0]][c[1]]=0
print(maxs)

