import sys
from collections import deque
input = sys.stdin.readline
INF = 10e8
dd = [[0,1],[0,-1],[1,0],[-1,0]]
def outLines(r,c):
    return 0 <= r < n and 0 <= c < n
count = 0
while True:
    count +=1
    n = int(input())
    if n == 0:
        break
    q = deque()
    q.append([0,0])
    graph= []
    tf = [[False] * n for _ in range(n)]
    save = [[INF] * n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    tf[0][0] = True  
    save[0][0] = graph[0][0]
    while q:
        r,c = q.popleft()
        for dr,dc in dd:
            ddr,ddc = dr + r , dc + c
            if outLines(ddr,ddc) and not tf[ddr][ddc]:
                save[ddr][ddc] = graph[ddr][ddc] + save[r][c]
                q.append([ddr,ddc])
                tf[ddr][ddc] = True
            elif outLines(ddr,ddc) and tf[ddr][ddc]:
                if save[ddr][ddc] > graph[ddr][ddc] + save[r][c]:
                    save[ddr][ddc] = graph[ddr][ddc] + save[r][c]
                    q.appendleft([ddr,ddc])
    print('Problem',end=" ")
    print(count,end="")
    print(':',end=" ")
    print(save[n-1][n-1])
    