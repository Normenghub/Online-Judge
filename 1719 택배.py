import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
front = [[] for _ in range(n+1)]
INF = 10e8
back = [0] * (n+1)
arr = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    front[a].append((c,b))
    front[b].append((c,a))

def daik(start):
    q= []
    heapq.heappush(q,(0,start))
    arr[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > arr[now]:
            continue
        for price,next_node in front[now]:
            if arr[next_node] > arr[now] + price:
                arr[next_node] = arr[now] + price
                back[next_node] = now
                heapq.heappush(q,(arr[next_node],next_node))
def findParents(v):
    global present,g
    if back[v] == 0:
        return v
    elif back[v] == g:
        return v
    else:
        return findParents(back[v])

maps = []
    
for i in range(1,n+1):
    g = i
    back = [0] * (n+1)
    arr = [INF] * (n+1)
    x = []
    daik(i)
    for k in range(1,n+1):
        if i == k :
            x.append('-')
            continue
        present = k
        x.append(findParents(k))
    maps.append(x)
for i in range(n):
    for k in range(n):
        print(maps[i][k],end=" ")
    print()