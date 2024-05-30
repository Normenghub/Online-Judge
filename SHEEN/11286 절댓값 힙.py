import sys
import heapq
input = sys.stdin.readline
n = int(input())
dic = {}
arr = []
for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(arr,abs(num))
        if num in dic:
            dic[num] +=1
        else:
            dic[num] =1     
    else:
        if len(arr) == 0:
            print(0)
        else:
           minNum = heapq.heappop(arr)
           if -minNum in dic and dic[-minNum] > 0:
               print(-minNum)
               dic[-minNum] -=1
           else:
               print(minNum)
               dic[minNum] -=1                               
