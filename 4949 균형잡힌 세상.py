from collections import deque
import sys
input = sys.stdin.readline
lists = deque()
strings = input()
strings = list(strings)


def solution(strings):
    for i in range(len(strings)):
        if strings[i] == '(' or '[':
            lists.append(strings[i])
        elif strings[i]==    



# 