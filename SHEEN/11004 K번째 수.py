import sys
import heapq
input = sys.stdin.readline
n,k = map(int,input().split())
arr = list(map(int,input().split()))
heapq.heapify(arr)
x = []
leng = len(arr)
for i in range(leng):
    x.append(heapq.heappop(arr))
print(x[k-1])