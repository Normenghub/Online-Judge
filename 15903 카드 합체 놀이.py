import heapq
import sys
input = sys.stdin.readline
n , m= map(int,input().split())
arr = list(map(int,input().split()))
heapq.heapify(arr)
for _ in range(m):
    card1 = heapq.heappop(arr)
    card2 = heapq.heappop(arr)
    sumCard = card1 + card2
    for two in range(2):
        heapq.heappush(arr,sumCard)
print(sum(arr))        