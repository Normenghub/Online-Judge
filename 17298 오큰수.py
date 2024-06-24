import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque(map(int,input().split()))
subArr = deque()
subArr.append(arr[-1])
currentValue = arr[-1]
save= deque()
save.append(-1)
arr.pop()
# 1 2 5 4 3 2 2 3 4 5 3 7 
# 5 5 7 5 4 3 3 4 5 7 7 -1
# 5 5 7 5 4 3 3 4 5 7 7 -1
for i in range(n-1):
    if arr[-1] < currentValue:
        save.appendleft(currentValue)
        currentValue = arr.pop()
        subArr.appendleft(currentValue)
    else:
        flag = False
        xx = len(subArr)
        for x in range(xx):
            currentValue = subArr.popleft()
            if currentValue > arr[-1]:
                save.appendleft(currentValue)
                subArr.appendleft(currentValue)
                currentValue = arr.pop()
                subArr.appendleft(currentValue)
                flag = True
                break
            else:
                continue    
        if flag == True:
            continue
        else:
          subArr = deque()
          subArr.append(arr[-1])
          currentValue = arr.pop()   
          save.appendleft(-1)  
         
for x in save:
    print(x,end=" ")     