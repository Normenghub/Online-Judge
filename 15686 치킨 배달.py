import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
queue =deque()
graph = []
df = 0
resultSum = []
dic = {}
n ,m = map(int,input().split())
for i in range(n):
   x = list(map(int,input().split()))
   for k in range(n):
       if x[k] == 1:
           df+=1
           queue.append([i,k])
       elif x[k] == 2:   
           dic[f'{i} {k}'] = []
   graph.append(x)

keyList = list(dic.keys())
dd =[[0,1],[0,-1],[1,0],[-1,0]]

def canGo(r,c):
    return 0<= r< n and 0 <= c < n

def bfs(graph,x,y, tf):
    xasd = deque([(x,y)])
    while xasd:
     tw , tq = xasd.popleft()
     for dr,dc in dd:
        ddr = dr+tw
        ddc = dc+tq
        if canGo(ddr,ddc) and not tf[ddr][ddc]:
            graph[ddr][ddc] = graph[tw][tq] +1
            tf[ddr][ddc] = True
            xasd.append([ddr,ddc])
        

while queue:
    tf = [[False] * n for i in range(n)]
    x,y = queue.popleft()
    tf[x][y] = True
    graph[x][y] = 0
    bfs(graph,x,y,tf)
    for a in range(len(keyList)):
        q,w = keyList[a].split()
        asd = graph[int(q)][int(w)]
        dic[f'{q} {w}'].append(asd)

lists = list(combinations(keyList,m))
result = 0


for r in range(len(lists)):
 result = 0
 for rr in range(df): # dic len two counted df
   x = 9999
   for rrr in range(m): # two 
    x = min(x, dic[lists[r][rrr]][rr])
   result += x
 resultSum.append(result)
print(min(resultSum))
