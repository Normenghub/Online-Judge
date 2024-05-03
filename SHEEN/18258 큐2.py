from collections import deque
import sys
input = sys.stdin.readline
lists = deque()
num = int(input())

for i in range(num):
    s = list(input().split())
    if s[0] == 'push':
        lists.append(s[1])
    elif s[0]  == 'front':
        if len(lists) == 0:
            print(-1)
        else:
            print(lists[0])
    elif s[0]  == 'back':
        if len(lists) == 0:
            print(-1)
        else:
            print(lists[-1])
    elif s[0] == 'size':
        print(len(lists))
    elif s[0]  == 'empty':                    
        if len(lists) == 0:
            print(1)
        else:
            print(0)
    elif s[0]  == "pop":
        if len(lists) == 0:
            print(-1)
        else:
            print(lists.popleft())                
