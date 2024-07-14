import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
time = 0
graph = []
zeroQueue = deque()
iceQueue = deque()
tf = [[False] * m for _ in range(n)]

def outLines(r,c):
   return 0<=r < n and 0 <= c < m

dd = [[0,1], [1,0], [-1,0],[0,-1]]

for i in range(n):
    x = list(map(int,input().split()))
    for k in range(m):
        if x[k] != 0:
            iceQueue.append([i,k])
        else:
            zeroQueue.append([i,k])
    graph.append(x)


zerolength = len(zeroQueue)
icelength = len(iceQueue)


def checkIce():
   global zerolength,icelength
   count = 0
   for _ in range(icelength):
    x,y = iceQueue.popleft()

    if graph[x][y] <= 0:
       graph[x][y] = 0
       icelength -=1
       zeroQueue.append([x,y])
       zerolength +=1
       continue
    iceQueue.append([x,y])
    if tf[x][y]:
       continue
    
    count +=1
    saveTf = deque()
    saveTf.append([x,y])
    while saveTf:
     xx,yy = saveTf.popleft()
   

     for dx,dy in dd:
        ddx = dx + xx
        ddy = dy + yy
        if outLines(ddx,ddy) and graph[ddx][ddy] != 0 and not tf[ddx][ddy]:
           tf[ddx][ddy] = True
           saveTf.append([ddx,ddy])
   return count 

def checkSea():
   global zerolength
   for _ in range(zerolength):
    dic = {}
    x , y  = zeroQueue.popleft()
    c = 0
    for dx,dy in dd:
       ddx = dx + x
       ddy = dy + y

       if outLines(ddx,ddy) and graph[ddx][ddy] != 0:
          if (ddx,ddy) not in dic: dic[(ddx,ddy)] = 1
          else:  dic[(ddx,ddy)] += 1
       else:
          c+=1
    if c == 4:
       zerolength -=1
       continue
    
    zeroQueue.append([x,y])
       
          
    for gx , gy in dic.keys():
        graph[gx][gy] -= dic[(gx,gy)]
    
flag = False
     
while icelength != 0:
   checkSea()
   time +=1
   count = checkIce()
   tf = [[False] * m for _ in range(n)]
   if count >=2:
      flag = True
      break
if flag:  print(time)
else:  print(0)

            
       



