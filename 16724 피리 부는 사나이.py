from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향에 대한 매핑
way = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# 입력 받기
n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]

# 방문 체크 배열
visited = [[False] * m for _ in range(n)]

# 경로 추적 배열
path = [[-1] * m for _ in range(n)]

def out_of_bounds(r, c):
    return 0 <= r < n and 0 <= c < m

def dfs(r, c, cnt):
    if path[r][c] != -1:  # 이미 현재 탐색에서 방문한 노드이면 사이클
        return path[r][c] == cnt

    if visited[r][c]:  # 다른 경로에서 이미 방문한 노드
        return False

    # 현재 노드 방문 처리
    visited[r][c] = True
    path[r][c] = cnt

    # 다음 방향으로 이동
    dr, dc = way[graph[r][c]]
    nr, nc = r + dr, c + dc

    # 다음 노드로 DFS
    if out_of_bounds(nr, nc):
        if dfs(nr, nc, cnt):
            return True

    # 경로 추적 해제
    path[r][c] = -1
    return False

cycle_count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, i * m + j):  # 고유의 카운트 값 전달
                cycle_count += 1

print(cycle_count)