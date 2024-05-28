import sys 
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque()
count = 0
for i in range(n):
    arr.appendleft(int(input()))
for x in range(1,len(arr)):
    if arr[x] < arr[x-1]:
        continue
    else:
        sub = abs(arr[x-1] - arr[x] -1)
        arr[x] -=sub
        count += abs(sub)
print(count)