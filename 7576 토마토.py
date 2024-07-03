import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int,input().split())
graph = []
countAll = 0
queue = deque()
for i in range(n):
    arr = list(map(int,input().split()))
    for k in range(m):
        if arr[k] == 1: 
         queue.append([i,k])
        elif arr[k] == 0:
           countAll +=1
           
    graph.append(arr)
dd = [[0,1],[0,-1],[1,0],[-1,0]]
def canGo(r,c):
    return 0<= r<= n-1 and 0<= c<=m-1
count = 0
point = 0
lenghs = len(queue)
while queue:
   r , c = queue.popleft()
   point +=1
   for dr,dc in dd:
       ddr = r+dr
       ddc = c+dc
       if canGo(ddr,ddc) and graph[ddr][ddc] == 0:
           countAll -=1
           graph[ddr][ddc]=1
           queue.append([ddr,ddc])
       elif canGo(ddr,ddc) and graph[ddr][ddc] == -1: continue
       elif canGo(ddr,ddc) and graph[ddr][ddc] == 1: continue
       else: continue
   if point==lenghs:
      count +=1
      lenghs += len(queue)
if countAll == 0: print(count-1)
else: print(-1)