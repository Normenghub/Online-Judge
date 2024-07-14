import sys
from collections import deque
input = sys.stdin.readline
num = int(input())
q = deque()
q.append([1,0])
visited = {}
visited['1 0'] = 0
while q:
    n , c = q.popleft()
    if n == num:
        print(visited[f'{n} {c}'])
        break
    if f'{n} {n}' not in visited.keys():
        visited[f'{n} {n}'] = visited[f'{n} {c}'] + 1
        q.append([n,n])
    if f'{n+c} {c}' not in visited.keys():
        visited[f'{n+c} {c}'] = visited[f'{n} {c}'] + 1
        q.append([n+c,c])
    if f'{n-1} {c}' not in visited.keys():
        visited[f'{n-1} {c}'] = visited[f'{n} {c}'] + 1
        q.append([n-1,c])

