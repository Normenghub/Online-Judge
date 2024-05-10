from collections import deque
n=int(input())
arr = deque(map(int,input().split()))
stack = deque()
wating = min(arr)
while len(arr)>0:
 if arr[0] == wating:
  arr.popleft()
  wating +=1
  if len(stack) >=1:
   for k in range(len(stack)):
    if stack[len(stack)-1] == wating:
     stack.pop()
     wating+=1
    else:
     break
 else:
  stack.append(arr.popleft())  
for k in range(len(stack)):
  if stack[len(stack)-1] == wating:
   stack.pop()
   wating +=1
  else:
   break 
 
if len(stack) ==0:
 print("Nice")
else:
 print("Sad") 