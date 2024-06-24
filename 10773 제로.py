from collections import deque
import sys
input = sys.stdin.readline

lists = deque()

num= int(input())

for i in range(num):
    a = int(input())
    if a == 0:
            lists.pop()
    else:
            lists.append(a)


print(sum(lists))            
