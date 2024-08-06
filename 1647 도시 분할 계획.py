import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())

result = 0
maxs = 0

q = []
arr=[[] for _ in range(v+1)]

tf = [False] * (v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    arr[a].append((c,b))
    arr[b].append((c,a))

def MST(start):
    tf[start] = True
    for i in arr[start]:
        heapq.heappush(q,i)
    while q:
        global result,maxs
        price, num = heapq.heappop(q)
        if tf[num]:
            continue
        tf[num] = True
        result += price
        maxs = max(maxs,price)
        for i in arr[num]:
            if tf[i[1]]:
                continue
            else:
                heapq.heappush(q,i)


MST(1)

print(result - maxs)