import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
queue2 = deque()
n = int(input())
graph = []
count = 1
count2 = 1
flag2 = ''
tf = []
tf2 = []
for i in range(n):
    c = list(input().rstrip())
    for w in range(len(c)):
        queue.append([i,w])
        queue2.append([i,w])
    s = [False] * n
    graph.append(c)
    tf.append(s)
def canGo(r,c):
    return 0<= r <= n-1 and 0<= c <= n-1
dd = [[0,1],[0,-1],[1,0],[-1,0]]
tf[0][0] = True
while queue:
    r,c = queue.popleft()
    flag = graph[r][c]
    if tf[r][c] == False:
        count +=1
    for dr,dc in dd:
        ddr = dr + r  
        ddc = dc + c
        if canGo(ddr,ddc) and graph[ddr][ddc] == flag and tf[ddr][ddc] == False:
            queue.appendleft([ddr,ddc])
            tf[ddr][ddc] = True
print(count)
for i in range(n):
    tf2.append([False] * n)
tf2[0][0] = True
while queue2:
    r,c = queue2.popleft()
    flag = graph[r][c]
    if tf2[r][c] == False:
        count2 +=1
    for dr,dc in dd:
        ddr = dr + r  
        ddc = dc + c
        if flag == 'R' or flag == 'G':
            if canGo(ddr,ddc) and tf2[ddr][ddc] == False:
               if graph[ddr][ddc] == 'R' or graph[ddr][ddc] == 'G': 
                queue2.appendleft([ddr,ddc])
                tf2[ddr][ddc] = True
        else:
            if canGo(ddr,ddc) and tf2[ddr][ddc] == False and graph[ddr][ddc] == flag:
                queue2.appendleft([ddr,ddc])
                tf2[ddr][ddc] = True
print(count2)


        

        


