import sys
from collections import deque
input = sys.stdin.readline

dd = [[0,1],[0,-1],[1,0],[-1,0]]

n , m = map(int,input().split())

def outLines(r,c):
    return 0 <= r < n and 0 <= c < m

graph = []

fireQueue = deque()
queue = deque()

for i in range(n):
    x = list(input().rstrip())
    for k in range(m):
        if x[k] == 'F':
            fireQueue.append([i,k])
        elif x[k] =='J':
            queue.append([i,k])
    graph.append(x)

tf =[[False] * m for _ in range(n)]

graph[queue[0][0]][queue[0][1]] = 0

while True:
    lenQueue = len(queue)
    s = lenQueue
    count = 0
    for i in range(len(queue)):

        r,c = queue.popleft()
        
        if graph[r][c] == 'F':
            count +=1
            continue
        
        for dr,dc in dd:
            ddr ,ddc = dr+r , dc+c
            if outLines(ddr,ddc) and not tf[ddr][ddc] and graph[ddr][ddc] =='.':
                tf[ddr][ddc] = True
                graph[ddr][ddc] = graph[r][c] +1 
                queue.append([ddr,ddc])
            elif not outLines(ddr,ddc):
                print(graph[r][c]+1)
                exit()
    if count == s:
        print('IMPOSSIBLE')
        exit()
    lenfire = len(fireQueue)
    for _ in range(lenfire):
        r,c = fireQueue.popleft()
        for dr,dc in dd:
            ddr ,ddc = dr+r , dc+c
            if outLines(ddr,ddc) and graph[ddr][ddc] != '#' and graph[ddr][ddc] !='F':
                graph[ddr][ddc] = "F"
                tf[ddr][ddc] = True
                fireQueue.append([ddr,ddc])
    
    


            


