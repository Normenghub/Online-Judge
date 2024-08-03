import heapq,sys
input = sys.stdin.readline

v,e = map(int,input().split())

INF = 10e8

k = int(input())

graph =[[] for _ in range(v+1)]
go = [INF] * (v+1)


for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def daik(start):
   q = []
   heapq.heappush(q,(0,start))
   go[start] = 0

   while q:
       a , b = heapq.heappop(q)
       if go[b] < a:
           continue
       for x in graph[b]:
           cost = x[1] + a
           if cost < go[x[0]]:
               go[x[0]] = cost
               heapq.heappush(q,(cost,x[0]))
daik(k)

for i in range(1,len(go)):
    if go[i] == 1000000000:
        print('INF')
    else:
        print(go[i])