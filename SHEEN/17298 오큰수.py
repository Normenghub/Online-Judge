from collections import deque
import sys 
input = sys.stdin.readline
n = int(input())
arr = deque()
save = []
for i in range(n):
    x = arr.popleft()
    