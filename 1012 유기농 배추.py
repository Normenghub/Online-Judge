import sys
sys.setrecursionlimit(10**7)
from collections import deque
input = sys.stdin.readline
dd = [[1,0],[-1,0],[0,1],[0,-1]]
def canGoto(ddr,ddc):
   return 0<= ddr <=m-1 and 0<= ddc <=n-1
       
def dfs(a,b,trueFalse,graph):
    trueFalse[a][b] = True
    for dr,dc in dd:
       ddr = dr+a
       ddc = dc+b
       if canGoto(ddr,ddc):
          if not trueFalse[ddr][ddc] and graph[ddr][ddc] == 1: 
           dfs(ddr,ddc,trueFalse,graph)
          else:
             continue
       else:
          continue
for _ in range(int(input())):
    m,n,k = map(int,input().split())
    graph = []
    queue = deque()
    trueFalse = []
    count = 0
    for i in range(m):
      arr = []
      cc = []
      for i in range(n):
         arr.append(0)
         cc.append(False)
      graph.append(arr)
      trueFalse.append(cc)
    for c in range(k):
       a, b = map(int,input().split())
       graph[a][b] = 1
       queue.append([a,b])
    while queue:
       v = queue.popleft()
       if trueFalse[v[0]][v[1]] == True:
          continue
       else:
        count +=1
        dfs(v[0],v[1],trueFalse,graph)
    print(count)
