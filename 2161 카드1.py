import sys
from collections import deque
arr = deque(i for i in range(1,int(input())+1))
save=[]
if len(arr) == 1:
    print(1)
    exit()
else:    
 while len(arr)!=1:
    save.append(arr.popleft())
    arr.append(arr.popleft())
save.append(arr[0])
for i in save:
   print(i,end = " ")    
