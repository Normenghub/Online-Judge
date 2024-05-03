from collections import deque
import sys
input = sys.stdin.readline

lists = deque()

num= int(input())


def solution(num,lists):
        strings = list(input().split())
        for k in range(len(strings)):
            try:
             if strings[k] == '(':
                 lists.append(k)
             else:
                 lists.pop()
            except:
                return "NO"
        return "Yes"        
        
for i in range(num):
    print(solution(num,lists))            
