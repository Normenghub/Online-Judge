import sys
import heapq
count = []
input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(str,input().split()))
front= [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    front[a].append((c,b))
    front[b].append((c,a))
visited = [False] * (n+1)
def checkSex(start,r,c):
    if arr[start-1] == 'W':
            if arr[c-1] =='M':
                heapq.heappush(q,(r,c))
    else:
            if arr[c-1] == 'W':
                heapq.heappush(q,(r,c))
q = []

def MST(start):
    visited[start] = True
    for r ,c in front[start]:
        checkSex(start,r,c)
    while q:
         r,c = heapq.heappop(q)
         if visited[c]:
              continue
         visited[c] = True
         count.append(r)
         for i in front[c]:
              if visited[i[1]]:
                   continue
              else:
                   checkSex(c,i[0],i[1])
MST(1)
if len(count)+1 != n:
     print(-1)
else:     
 print(sum(count))

    