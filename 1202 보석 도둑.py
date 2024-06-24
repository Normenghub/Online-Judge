import sys
import heapq
input = sys.stdin.readline
Ci = []
save = []
result = 0
N, K = map(int,input().split())
dic = [list(map(int,input().split())) for _ in range(N)]
Ci = [int(input().strip()) for _ in range(K)]
dic.sort()
Ci.sort()

for asd in Ci:
    while dic and dic[0][0] <= asd:
        heapq.heappush(save, -dic[0][1])
        heapq.heappop(dic)
        
    if save:
        result -= heapq.heappop(save)
    print(dic)
print(result)


