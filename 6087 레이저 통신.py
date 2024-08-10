import sys
input = sys.stdin.readline
from collections import deque

m , n = map(int,input().split())
graph = []
q = deque()
for  i in range(n):
    x = list(input().rstrip())
    for k in range(m):
        if x[k] == 'C':
            q.append([i,k])
    graph.append(x)

r,c = q.popleft()
graph[r][c] = (None,0)
q.append((r,c))
finalx,finaly = q.popleft()
def outLines(r,c):
   return 0 <= r <  n and 0<= c < m
dd = [[0,1],[0,-1],[1,0],[-1,0]]
def checkDirection(r,c,ddr,ddc,direction,count):
   l = []
   if r == ddr:
      if c > ddc:
         if direction == 2 or direction == None:
            l.append(2)
            l.append(count)
         else:
            l.append(2)
            l.append(count+1)
      else:
         if direction == 3 or direction == None:
            l.append(3)
            l.append(count)
         else:
            l.append(3)
            l.append(count+1)
   else:
      if r > ddr:
         if direction == 0 or direction == None:
            l.append(0)
            l.append(count)
         else:
            l.append(0)
            l.append(count+1)
      else:
         if direction == 1 or direction == None:
            l.append(1)
            l.append(count)
         else:
            l.append(1)
            l.append(count+1)
   return l
while q:
   r,c = q.popleft()
   for dr , dc in dd:
      ddr ,ddc = dr + r , dc + c
      if outLines(ddr,ddc) and graph[ddr][ddc] != '*':
         arr = checkDirection(r,c,ddr,ddc,graph[r][c][0],graph[r][c][1])
         if graph[ddr][ddc] == '.' or graph[ddr][ddc] == 'C':
            graph[ddr][ddc] = (arr[0],arr[1])
            q.appendleft((ddr,ddc))
         elif graph[ddr][ddc][1] >= arr[1]:
            graph[ddr][ddc] = (arr[0],arr[1])
            q.append((ddr,ddc))
         


print(graph[finalx][finaly][1])

             


   



