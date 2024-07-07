import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

if n == k:
    print(0)
    print(n)
    exit()

max_range = 200000 
tf = [False] * (max_range + 1)
move = [0] * (max_range + 1)

queue = deque()
queue.append(n)
count = 0

tf[n] = True
dw = deque()

while queue:
    val = queue.popleft()
    for i in (val + 1, val - 1, val * 2):
        if 0 <= i <= max_range and not tf[i]:
            tf[i] = True
            dw.append(i)
            move[i] = val
    if tf[k]:
        break
    if not queue:
        count += 1
        for _ in range(len(dw)):
            queue.append(dw.popleft())

print(count + 1)

xw = [k]
x = -1
while x != n:
    x = move[k]
    xw.append(x)
    k = x

for i in range(len(xw) - 1, -1, -1):
    print(xw[i], end=" ")
