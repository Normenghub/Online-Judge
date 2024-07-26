import sys
from collections import deque
input = sys.stdin.readline

graph = []
tf = []
n,m = map(int,input().split())

if n==1 and m == 1:
    print(1)
    exit()

queue = deque()

for i in range(n):
    x = list(input().rstrip())
    c = []
    graph.append(x)
    for k in range(m):
        c.append([False,False])
    tf.append(c)
    
queue.append([0,0,0])
tf[0][0][0] = 0 

def outLines(r,c):
    return 0<= r < n and 0 <= c < m

dd = [[0,1],[0,-1],[1,0],[-1,0]]

while queue:
    q,w,e = queue.popleft()
    for dq,dw in dd:
        ddq = dq+q
        ddw = dw+w
        if outLines(ddq,ddw) and not tf[ddq][ddw][e]:
         if graph[ddq][ddw] == '1' and e == 0:
             queue.append([ddq,ddw,e+1])
             tf[ddq][ddw][e+1] = tf[q][w][e] + 1
         

         elif graph[ddq][ddw] == '0':
             queue.append([ddq,ddw,e])
             tf[ddq][ddw][e] = tf[q][w][e] + 1
if not tf[n-1][m-1][0] and not tf[n-1][m-1][1]:
    print(-1)
elif not tf[n-1][m-1][0] or not tf[n-1][m-1][1]:
    if not tf[n-1][m-1][0]:
        pass
    else:
        print(tf[n-1][m-1][0]+1)
    if not tf[n-1][m-1][1]:
        pass
    else:
        print(tf[n-1][m-1][1]+1)
else:
    print(min(tf[n-1][m-1][0]+1,tf[n-1][m-1][1]+1))
    