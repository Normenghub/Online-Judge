import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque()
result = 0
if n == 1:
  print(1)
  exit()
else:
  for i in range(1,n+1):
    if n % i == 0:
      arr.append(i)
  for x in arr:
    c = []
    for q in range(1,x+1):
      if x % q == 0:
        c.append(q)
    result += sum(c)
    continue
print(result)      
      
      



     