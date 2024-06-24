import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr = deque()
temp = 1
saveArr = deque()
for i in range(1,n+1):
    arr.append(i)   

while len(arr) >0:
   if temp !=m:
       arr.append(arr.popleft())
       temp +=1
   else:
       saveArr.append(arr.popleft())
       temp =1
print('<',end="")
for k in range(len(saveArr)-1):
 print(saveArr[k],end=", ")
print(f'{saveArr[len(saveArr)-1]}>') 

