import sys
input = sys.stdin.readline
import heapq
arr = []
n = int(input())
for i in range(n):
    a= int(input())
    if a == 0:
        if len(arr) ==0:
            print(0)
        else:
         result = heapq.heappop(arr)
         print(result)
    else:
         heapq.heappush(arr, a)        