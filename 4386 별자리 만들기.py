import sys
import heapq
from collections import deque
import math

input = sys.stdin.readline

n = int(input())
coordinates = []
for _ in range(n):
    coordinates.append(list(map(float, input().split())))

# Create graph: adjacency list of (cost, node)
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist = math.sqrt((coordinates[j][1] - coordinates[i][1])**2 + (coordinates[j][0] - coordinates[i][0])**2)
            graph[i].append((dist, j))

def prim(start):
    visited = [False] * n
    min_heap = []
    result = 0.0

    # Start from the given node
    for cost, neighbor in graph[start]:
        heapq.heappush(min_heap, (cost, neighbor))

    visited[start] = True
    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if not visited[node]:
            visited[node] = True
            result += cost
            for next_cost, neighbor in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (next_cost, neighbor))
    
    return result

# Start MST from node 0 (can be any node)
mst_cost = prim(0)
print(f"{mst_cost:.2f}")