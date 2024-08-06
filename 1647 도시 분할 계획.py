import sys
import heapq
input = sys.stdin.readline

n , k =map(int,input().split())

arr = [[] for _ in range(n+1)]
tf = [False] * (k+1)
tree = [0] * (k+1)

q = []
result = 0
maxs= 0

for _ in range(k):
    a,b,c = map(int,input().split())
    arr[a].append((c,b))
def MST(v):
    global maxs
    
    tf[v] = True
    for i in arr[v]:
        heapq.heappush(q,i)
    while q:
        price,start = heapq.heappop(q)
        if tf[start]:
            continue
        tf[start] = True
        result +=price
        maxs = max(maxs,price)
        for i in arr[start]:
            if not tf[i[1]]:
                heapq.heappush(q,i)

MST(1)
print(result - maxs)
    
