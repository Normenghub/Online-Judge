from collections import deque
import sys
input = sys.stdin.readline
arr = deque()
n = int(input())
for i in range(n):
    s= list(map(str,input().rstrip().split()))
    if s[0]=="push_back":
        arr.append(int(s[1]))
    elif  s[0]=="push_front" :
        arr.appendleft(int(s[1]))
    elif s[0] == "pop_front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif s[0] == "pop_back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop()) 
    elif s[0] == 'size':
        print(len(arr))
    elif s[0] =='empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    else:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])                                                          