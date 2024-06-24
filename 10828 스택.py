from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = deque()
for i in range(n):
    s = list(input().split())
    if s[0] == 'push':
        arr.append(int(s[1]))
    elif s[0] == 'pop':
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)    
    elif s[0] == 'size':
        print(len(arr))
    elif s[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'top':
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)                                           
       