import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
if n==k:
    print(0)
    exit()
tf = [False] * 1000001
queue = deque()
queue.append(n)
count = 0
val = 0
tf[n] == True
dw = deque()
while queue:
    val = queue.popleft()
    if 100000>=val-1 >=0 and tf[val-1] == False:
        tf[val-1] = True
        dw.append(val-1)
    if 100000>=val+1 >=0 and tf[val+1] == False:

        tf[val+1] = True
        dw.append(val+1)
    if 100000>=val*2 >=0 and tf[val*2] == False:
        tf[val*2] = True
        dw.append(val*2)
    if tf[k] == True:
        break
    if len(queue) == 0:
        count +=1
        for i in range(len(dw)):
            queue.append(dw.popleft())
      
print(count+1)