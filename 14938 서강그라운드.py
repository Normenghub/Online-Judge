import sys
input =sys.stdin.readline
import heapq
INF = 10e8
n,m,r = map(int,input().split())
front = [[] for _ in range(n+1)]
arr = list(map(int,input().split()))
for _ in range(r):
 a,b,c = map(int,input().split())
 front[a].append((c,b))
 front[b].append((c,a))
answer =[]

def daik(start):
 global m
 visited =[False] * (n+1)
 re = 0
 distance = [INF] * (n+1)
 distance[start] = 0
 q = []
 heapq.heappush(q,(0,start))
 while q:
  r,c =heapq.heappop(q)
  if visited[c]:
   continue
  visited[c] = True
  for a, b in front[c]:
    cost = distance[c] + a
    if cost < distance[b]:
     distance[b] = cost
     heapq.heappush(q,(cost,b))
 for i in range(1,n+1):
  if distance[i] <= m:
   re+= arr[i-1]
 return re

  
for i in range(1,n+1):
  answer.append(daik(i))

print(max(answer))