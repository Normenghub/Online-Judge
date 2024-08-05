import sys
import heapq
input = sys.stdin.readline  

n , m = map(int,input().split())

front = [[] for _ in range(n+1)]
back = [[] for _ in range(n+1)]
backCount = [0] * (n+1)
q = []
sequence = []

for i in range(m):
    a,b = map(int,input().split())
    front[a].append(b)
    back[b].append(a)
    backCount[b] +=1

for i in range(1,n+1):
    if backCount[i] == 0:
        q.append(i)
    else:
        back[i].sort()
while q:
    x = heapq.heappop(q)
    sequence.append(x)
    for i in front[x]:
        backCount[i] -=1
        if backCount[i] == 0:
            heapq.heappush(q,i)
for i in sequence:
    print(i,end=" ")
        




