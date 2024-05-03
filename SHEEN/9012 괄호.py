from collections import deque
import sys
input = sys.stdin.readline

lists = deque()

num= int(input())

def solution(num):
        lists = deque()
        strings = input()
        strings = list(strings)
        del strings[-1]
        
        for k in range(len(strings)):
             if strings[k] == '(':
                 lists.append(strings[k])
             else:
                 if len(lists) > 0:
                     lists.pop()
                 else:
                     
                   return "NO"
        if len(lists)>0:
                     return "NO"
        else:
                   return "YES"        
        
for i in range(num):
    print(solution(num))            
