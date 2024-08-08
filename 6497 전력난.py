import sys
import heapq
input = sys.stdin.readline

while True:
 v,e =map(int,input().split())
 if v ==0 and e == 0:
    break
 result = 0
 count = 0
 q = []
 arr=[[] for _ in range(v+1)]
 asd = [0] * (v)

 tf = [False] * (v)

 for _ in range(e):
    a,b,c = map(int,input().split())
    arr[a].append((c,b))
    arr[b].append((c,a))
    count += c



 def MST(start):
    tf[start] = True
    for i in arr[start]:
        heapq.heappush(q,i)
    while q:
        global result
        price, num = heapq.heappop(q)
        if tf[num]:
            continue
        tf[num] = True
        result += price
        for i in arr[num]:
            if tf[i[1]]:
                continue
            else:
                heapq.heappush(q,i)
                


 MST(0)

 print(count - result)

# 7 9 15 8 11 50