import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
minhigh = 101
maxhigh = -1
graph = []

for i in range(n):
    arr = list(map(int, input().split()))
    for height in arr:
        if height < minhigh: minhigh = height
        if height > maxhigh: maxhigh = height
    graph.append(arr)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def canGo(a, b):
    return 0 <= a < n and 0 <= b < n

def bfs(start_a, start_b, height, tf):
    queue = deque([(start_a, start_b)])
    tf[start_a][start_b] = True
    while queue:
        a, b = queue.popleft()
        for dr, dc in directions:
            ddr, ddc = a + dr, b + dc
            if canGo(ddr, ddc) and graph[ddr][ddc] > height and not tf[ddr][ddc]:
                tf[ddr][ddc] = True
                queue.append((ddr, ddc))

result = 0

for height in range(minhigh - 1, maxhigh):
    tf = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not tf[i][j] and graph[i][j] > height:
                bfs(i, j, height, tf)
                count += 1
    result = max(result, count)

print(result)
