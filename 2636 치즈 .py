import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
count = 0
cqwe = 0
graph = []
result = []
for i in range(n):
   qwe = list(map(int,input().split()))
   for k in range(m):
      if qwe[k] == 1:
         cqwe +=1
   graph.append(qwe)
def outLines(r,c):
   return 0 <=r<= n-1 and 0<=c<=m-1
result.append(cqwe)
dd= [[0,1],[0,-1],[1,0],[-1,0]]

def airBFS(graph,dd):
    global count,cqwe,result
    v = []
    queue =deque()
    queue.append([0,0])
    tf = [[False] * m for _ in range(n)]
    tf[0][0] = True
    while queue:
        r,c = queue.popleft()

        for dr,dc in dd:
          ddr = dr+r
          ddc = dc +c
          if outLines(ddr,ddc) and graph[ddr][ddc] == 1 and not tf[ddr][ddc]:
             v.append([ddr,ddc])
             tf[ddr][ddc] = True
          elif outLines(ddr,ddc) and graph[ddr][ddc] == 0 and not tf[ddr][ddc]:
             queue.append([ddr,ddc])
             tf[ddr][ddc] = True
    for x ,y in v:
       graph[x][y] = 0
       cqwe -=1
    count +=1
    result.append(cqwe)


while True:
   airBFS(graph,dd) 
   if cqwe == 0:
      break
print(count)
if len(result) == 1:
   print(result[-1])
else:
   print(result[-2])

