import sys
from collections import deque
input = sys.stdin.readline

graph = []

n = int(input())

flag = False
experination = 0
PresentLevel = 2
result = 0

for i in range(n):
    x = list(map(int,input().split()))
    if not flag:
     for k in range(n):
        if x[k] == 9:
            sharkx = i
            sharky = k
            flag = True
            x[k] = 0
    graph.append(x)


tf = [[0] * n for _ in range(n)]

dd = [[0,1],[0,-1],[1,0],[-1,0]]

def outLines(r,c):
   return 0 <= r < n and 0<= c < n


def levelUpCheck():
   global experination,PresentLevel
   experination+=1
   if experination == PresentLevel:
      experination = 0
      PresentLevel +=1


queue = deque()
queue.append([sharkx,sharky])

directions = deque()
while True:
 while queue:
   r,c = queue.popleft()
   
   for dr,dc in dd:
      ddr , ddc  = dr + r , dc + c
      if outLines(ddr,ddc) and graph[ddr][ddc] == 0 and tf[ddr][ddc] == 0:
         tf[ddr][ddc] = tf[r][c] + 1
         queue.append([ddr,ddc])
      elif outLines(ddr,ddc) and 0< graph[ddr][ddc] <=PresentLevel and tf[ddr][ddc] == 0:
         tf[ddr][ddc] = tf[r][c] + 1
         if graph[ddr][ddc] < PresentLevel:
            if len(directions) == 0:
               directions.append([tf[ddr][ddc],ddr,ddc])
            else:
               if directions[0][0] > tf[ddr][ddc]:
                  directions = deque()
                  directions.append((tf[ddr][ddc],ddr,ddc))
               elif directions[0][0] == tf[ddr][ddc]:
                  directions.appendleft((tf[ddr][ddc],ddr,ddc))
         else:
            tf[ddr][ddc] = tf[r][c] + 1
            queue.append([ddr,ddc])
 if len(directions) == 0: break
 else: directions = sorted(directions,key = lambda x: (x[1] , x[2]))

 result += directions[0][0]
 levelUpCheck()
 graph[directions[0][1]][directions[0][2]] = 0
 sharkx = directions[0][1]
 sharky = directions[0][2]
 queue.append([sharkx,sharky])
 directions = deque()

 tf = [[0] * n for _ in range(n)]
 



print(result)


            
            
             
   
      





