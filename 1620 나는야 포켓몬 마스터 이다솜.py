#from collections import deque
import sys
input = sys.stdin.readline
nomordic = {}
lists = []

num, quest = map(int,input().split())

for i in range(num):
    s = input()
    nomordic[s] =i+1
    lists.append(s)

for k in range(quest):
    question = input()
    if question in nomordic:
        print(nomordic[question])
    else:
        print(lists[int(question)-1][:-1])    

