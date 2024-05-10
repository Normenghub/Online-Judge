import sys
input = sys.stdin.readline
import heapq

n = int(input())
saveheap = []
for i in range(n):
   num = int(input())
   if num == 0:
     if len(saveheap) ==0:
       print(0)
     else:  
      x= heapq.heappop(saveheap)
      print(-x)
   else:
    heapq.heappush(saveheap, -num)

