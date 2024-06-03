import sys
import heapq
timeTable = []
input = sys.stdin.readline
timeTable2 = []
n = int(input())
for i in range(n):
 start, end = map(int,input().split())
 timeTable2.append([start,end])
timeTable2.sort(key=lambda x: (x[0],x[1])) 
for k in range(len(timeTable2)):

 if len(timeTable) == 0:
  heapq.heappush(timeTable,timeTable2[k][1])
 else:
  minEnd = heapq.heappop(timeTable)
  if minEnd > timeTable2[k][0]:
    heapq.heappush(timeTable,timeTable2[k][1])
    heapq.heappush(timeTable,minEnd)
  else:
    heapq.heappush(timeTable,timeTable2[k][1])
print(len(timeTable))