'''
import sys 
input = sys.stdin.readline
from collections import deque
result = 0

n = int(input())
lists = deque()
for i in range(n):
  a = int(input())
  lists.append(a)
lists = deque(sorted(lists))
if n ==2:
   print(lists[0]+lists[1])
   exit()
elif n == 1:
   print(lists[0])
   exit()
elif n ==3:
  print(lists[0]+lists[1]+lists[2]+lists[0]+lists[1])
  exit()   
 
lists2  = deque()
lists2.append(lists[0] + lists[1])
result += lists[0] + lists[1]
lists.popleft()
lists.popleft()
while True:
 while len(lists) > 1:
    if len(lists2) == len(lists) == 1:
      break
    if lists2[0] > lists[1]:
     lists2.append(lists[0] + lists[1])
     result +=lists[0] + lists[1]
     lists.popleft()
     lists.popleft()
    else:
      lists2.append(lists[0] + lists2[0])
      result += (lists[0] + lists2[0])
      lists.popleft()
      lists2.popleft()
 if len(lists2) ==1 and len(lists) == 1:
     result +=(lists2[0] + lists[0])
     break
 elif len(lists2) == 2 and len(lists) == 0:
   result += (lists2[0] + lists2[-1])
   break
 elif len(lists) == 2 and len(lists2) == 0:
   result += (lists[0] + lists[-1])
   break 
 result += (lists[0] + lists2[0])
 lists.append(lists[0] + lists2[0])
 lists2.popleft()
 lists.popleft()
 if len(lists2) ==1 and len(lists) == 1:
     result +=(lists2[0] + lists[0])
     break
 elif len(lists2) == 2 and len(lists) == 0:
   result += (lists2[0] + lists2[-1])
   break
 elif len(lists) == 2 and len(lists2) == 0:
   result += (lists[0] + lists[-1])
   break 
 lists.append(lists2[0] + lists2[1])
 result += lists2[0] + lists2[1]
 lists2.popleft()
 lists2.popleft()
 if len(lists2) ==1 and len(lists) == 1:
     result +=(lists2[0] + lists[0])
     break
 elif len(lists2) == 2 and len(lists) == 0:
   result += (lists2[0] + lists2[-1])
   break
 elif len(lists) == 2 and len(lists2) == 0:
   result += (lists[0] + lists[-1])
   break 
 while len(lists2) >1:
    if len (lists2) == len(lists) == 1:
      break
    if lists[0] > lists2[1]:
     lists.append(lists2[0] + lists2[1])
     result +=lists2[0] + lists2[1]
     lists2.popleft()
     lists2.popleft()
    else:
      lists.append(lists[0] + lists2[0])
      result += (lists[0] + lists2[0])
      lists.popleft()
      lists2.popleft() 
 if len(lists2) ==1 and len(lists) == 1:
     result +=(lists2[0] + lists[0])
     break
 elif len(lists2) == 2 and len(lists) == 0:
   result += (lists2[0] + lists2[-1])
   break
 elif len(lists) == 2 and len(lists2) == 0:
   result += (lists[0] + lists[-1])
   break 


 
print(result)
'''

import sys 
input = sys.stdin.readline    
import heapq
result = 0
n = int(input())
lists = []
for i in range(n):
  a = int(input())
  lists.append(a)
lists.sort()
heapq.heapify(lists)
for k in range(n-1):
  m = heapq.heappop(lists)
  M = heapq.heappop(lists)
  heapq.heappush(lists, m+M)
  result += m+M

print(result)