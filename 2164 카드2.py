import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque()
for i in range(1,n+1):
    arr.append(i)    
while True:
    if len(arr) ==1:
        break
    else:
        arr.popleft()
    if len(arr) ==1:
        break
    else:
        arr.append(arr.popleft())

print(arr[0])