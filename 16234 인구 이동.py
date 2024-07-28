import sys
import copy
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline 
n,L,R = map(int,input().split())

tf = [[False] * n for _ in range(n)]

queue = deque()
graph = []
flag = True
for i in range(n):
    xx = list(map(int,input().split()))
    for k in range(n):
        queue.append([i,k])
    graph.append(xx)

copyQueue = copy.deepcopy(queue)

saveQueue = deque()
recount = 0
result = 0
count = 0
sumCount = 0
def outLines(r,c):
    return 0<=r< n and 0<= c < n

dd = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(tf,r,c):
    global count , sumCount 
    for dr,dc in dd:
        ddr = dr + r
        ddc = dc + c
        if outLines(ddr,ddc) and not tf[ddr][ddc] and L<= abs(graph[ddr][ddc] - graph [r][c]) <= R:
            tf[ddr][ddc] = True
            count +=1
            sumCount += graph[ddr][ddc]
            saveQueue.append([ddr,ddc])
            dfs(tf,ddr,ddc)
while True:
 while queue:
 
  r,c = queue.popleft()
  if not tf[r][c]:
     recount +=1
     tf[r][c]= True
     count = 1
     sumCount = graph[r][c]
     saveQueue.append([r,c])
     dfs(tf,r,c)
     for _ in range(len(saveQueue)):
         q,w = saveQueue.popleft()
         graph[q][w] = (sumCount//count)
    
  if recount == n*n:
     flag = False
     break
 if not flag:
    break
 result +=1
 recount = 0 
 tf = [[False] * n for _ in range(n)]
 queue = copy.deepcopy(copyQueue)

print(result)



    




