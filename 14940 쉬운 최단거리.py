import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
queue = deque()
graph = []
tf = []

dd = [[0,1],[0,-1],[1,0],[-1,0]]
def canGo(r,c):
    return 0 <= r<=n-1 and 0<=c<=m-1
for i in range(n):
      c = list(map(int,input().split()))
      f = [False]*m
      for z in range(m):
            if c[z] == 2:
               queue.append([i,z])

      graph.append(c)
      tf.append(f)
graph[queue[0][0]][queue[0][1]] = 0
tf[queue[0][0]][queue[0][1]] = True
while queue:
 r,c = queue.popleft()
 for dr,dc in dd:
    ddr = r + dr
    ddc = c + dc
    if canGo(ddr,ddc) and tf[ddr][ddc] != True and graph[ddr][ddc] != 0:
       graph[ddr][ddc] = graph[r][c] + 1
       tf[ddr][ddc] = True
       queue.append([ddr,ddc])
for i in range(n):
      for k in range(m):
          if graph[i][k] == 1 and tf[i][k] == False:
              print(-1,end=" ")
          else:
              print(graph[i][k],end=" ")
      print()