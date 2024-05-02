from collections import deque
import sys
input = sys.stdin.readline
q = deque()

num = int(input())

for i in range(num):
    strings = input()
    if strings[0] == "1":
        q.append(int(strings[2]))
    elif strings[0] == "2":  
        if len(q) == 0:
            print("-1")
        else:
            print(q.pop())
    elif strings[0] == "3":
        print(len(q))           
    elif strings[0] == "4": 
        if len(q) == 0:
            print(1)
        else:
            print(0)
    else:
          if len(q) == 0:
              print(-1)
          else:
            print(q[-1])