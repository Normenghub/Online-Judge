import sys
from collections import deque
input = sys.stdin.readline

n , k = map(int,input().split())

tf = [False] * (n +1)
q = deque()
front = [[] for _ in range(n+1)]
back = [0] * (n+1)
sequence = []

for _ in range(k):
    arr= deque(map(int,input().split()))
    x = arr.popleft()
    if len(arr) == 1:
        continue
    for i in range(x-1):
        front[arr[i]].append(arr[i+1])
        back[arr[i+1]]+=1
for i in range(1,n+1):
    if back[i] == 0:
        q.append(i)
while q:
    x = q.popleft()
    sequence.append(x)
    tf[x] = True
    for i in front[x]:
        back[i] -=1
        if back[i] == 0 and not tf[i]:
            q.append(i)
if len(sequence) != n:
    print(0)
else:
    for i in sequence:
        print(i)

