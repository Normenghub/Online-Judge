import sys
from collections import deque
input = sys.stdin.readline

dd = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,1],[1,-1]]

def outLines(r,c): return 0 <= r < h and 0 <= c < w

while True:
 w,h = map(int,input().split())
 result = 0
 if w == 0 and h== 0 : break

 else: 
  landQueue = deque()
  graph = []

  for i in range(h):
    x = list(map(int,input().split()))
    for k in range(w):
     if x[k] == 1:
      landQueue.append([i,k])
    graph.append(x)

  if len(landQueue) == 0 :
   print(0)
   continue

  while landQueue:
   saveQueue = deque()
   r,c = landQueue.popleft()

   if graph[r][c] == 'T':
    continue
   
   saveQueue.append([r,c])

   while saveQueue:
    
    r,c = saveQueue.popleft()
    graph[r][c] = 'T'

    for dr,dc in dd:
     ddr = dr + r
     ddc = dc + c
     if outLines(ddr,ddc) and graph[ddr][ddc] == 1:
      saveQueue.append([ddr,ddc])
   result +=1

 print(result)



   

  
  
      

