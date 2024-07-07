import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
if n==k:
    print(0)
    print(1)
    exit()
tf = [False] * 100001
queue = deque()
queue.append(n)
count = 0
val = 0
tf[n] = 0
dw = deque()
while queue:
    val = queue.popleft()
    if k == val:
        count +=1
    if 100000>=val-1 >=0:
     if tf[val-1] == False or tf[val-1] >= tf[val] + 1:
        tf[val-1] = tf[val] +1
        queue.append(val-1)
    if 100000>=val+1 >=0: 
     if tf[val+1] == False or tf[val+1] >= tf[val] + 1:
        tf[val+1] = tf[val] +1
        queue.append(val+1)
    if 100000>=val*2 >=0: 
      if tf[val*2] == False or tf[val*2] >= tf[val] + 1:
        tf[val*2] = tf[val] +1
        queue.append(val*2)

print(tf[k])
print(count)
# 1 2 2