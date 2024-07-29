import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = []

maxs = 0


tf = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(input().rstrip()))

dd = [[0,1],[0,-1],[1,0],[-1,0]]

def outLines(r,c):
    return 0<=r<n and 0 <= c < m

def dfs(tf,r,c,dic):
   global maxs 

   tf[r][c] = True
   for dr , dc in dd:
       ddr , ddc = dr+r , dc + c
       if outLines(ddr,ddc) and not tf[ddr][ddc] and graph[ddr][ddc] not in dic:
           dic[graph[ddr][ddc]] = True
           tf[ddr][ddc] = True
           dfs(tf,ddr,ddc,dic)
           dic.pop(graph[ddr][ddc])
       elif outLines(ddr,ddc) and not tf[ddr][ddc] and graph[ddr][ddc] in dic:
           maxs = max(len(dic),maxs)
           
   tf[r][c] = False


dfs(tf,0,0,{graph[0][0] : True})

print(maxs)
    