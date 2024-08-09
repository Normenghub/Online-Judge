import sys,heapq
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
k = int(input())
INF = 10e8
front = [[] for _ in range(n+1)]
back = [0] * (n+1)
for _ in range(k):
    a,b,c = map(int,input().split())
    front[a].append((c,b))
start , end = map(int,input().split())
arr = [INF] * (n+1)
road = []
    
q = []
arr[start] = 0

def daik(start):

    heapq.heappush(q,(0,start))
    while q:
        price, node = heapq.heappop(q)
        if arr[node] < price:
            continue
        for r,c in front[node]:
            if arr[c] > arr[node] + r:
                arr[c] = arr[node] + r
                back[c] = node
                heapq.heappush(q,(r,c))
def findRoad(v):
    if back[v] == 0:
        road.append(v)
        return 
    else:
        road.append(v)
        findRoad(back[v])

            
daik(start)
print(arr[end])
findRoad(end)
print(len(road))
for i in range(len(road)-1,-1,-1):
    print(road[i], end =" ")
