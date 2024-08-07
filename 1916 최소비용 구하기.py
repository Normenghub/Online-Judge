import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 10e8
front = [[]for _ in range(N+1)]

result = [0] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    front[a].append((c,b))

start,end=map(int,input().split())
visited =[False] * (N+1)

def daik(v):
    arr = [INF] * (N+1)
    arr[v] = 0
    q = []
    heapq.heappush(q,(0,v))

    while q:
        price , now_node = heapq.heappop(q)
        if visited[now_node]:
            continue
        visited[now_node] = True
        
        for r,next_node in front[now_node]:
            if arr[next_node] > arr[now_node] + r:
                arr[next_node] = arr[now_node] + r
                heapq.heappush(q,(arr[next_node],next_node))
    return arr

x = daik(start)
print(x[end])

            
