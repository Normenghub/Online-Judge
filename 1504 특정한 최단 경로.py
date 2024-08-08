import sys
import heapq
input = sys.stdin.readline

n,m=  map(int,input().split())

front = [[] for _ in range(n+1)]
INF = 10e8
answer =[]

for _ in range(m):
    a,b,c = map(int,input().split())
    front[a].append((c,b))
    front[b].append((c,a))
viaStart,viaEnd = map(int,input().split())

def daik(start):
    visited = [False] *  (n+1)
    arr=[INF] * (n+1)
    q = []
    arr[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        price,startnode = heapq.heappop(q)

        for r,c in front[startnode]:
            if arr[c] > arr[startnode] + r:
                arr[c] = arr[startnode] + r
                heapq.heappush(q,(arr[c],c))
    return arr

answer.append(daik(1)[viaStart] + daik(viaStart)[viaEnd] + daik(viaEnd)[n])
answer.append(daik(1)[viaEnd] + daik(viaEnd)[viaStart] + daik(viaStart)[n])
if min(answer) >=INF:
    print(-1)
else:
    print(min(answer))

# 경우의 수
'''
1  a  b n

1  b  a n





'''

    

    
