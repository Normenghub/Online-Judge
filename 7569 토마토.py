import sys
input = sys.stdin.readline
from collections import deque
graph = []
tf = []
queue = deque()
m,n,h = map(int,input().split())
for x in range(h):
    c = []
    tc = []
    for i in range(n):
     s = list(map(int,input().split()))
     ts = [False] * m
     for k in range(len(s)):
        if s[k] == 1:
           queue.append([x,i,k])
     c.append(s)
     tc.append(ts)
    graph.append(c)
    tf.append(tc)
maxs = 0
def canGo(r,c,h2):
   return 0<=r<=n-1 and 0<=c<=m-1 and 0<=h2<=h-1 
dd = [[-1,0,0],[1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
while queue:
   h2,r,c= queue.popleft()
   tf[h2][r][c] = True
   for dh ,dr ,dc in dd:
      ddh = h2 + dh
      ddr = dr + r
      ddc = dc + c
      if canGo(ddr,ddc,ddh) and not tf[ddh][ddr][ddc] and graph[ddh][ddr][ddc] == 0:
         tf[ddh][ddr][ddc] = True
         graph[ddh][ddr][ddc] = graph[h2][r][c] +1
         maxs = max(maxs,graph[ddh][ddr][ddc])
         queue.append([ddh,ddr,ddc])
for x in range(h):
   for i in range(n):
      for k in range(m):
         if graph[x][i][k] == 0 and not tf[x][i][k]:
            print(-1)
            exit()
if maxs >= 2:
   print(maxs-1)
else:
   print(maxs)
   
