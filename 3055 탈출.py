import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
queue = deque()

# 초기 설정
for i in range(n):
    z = list(input().rstrip())
    for k in range(m):
        if z[k] == '*':
            queue.append((i, k, '*'))
        elif z[k] == 'S': 
            startx, starty = i, k
        elif z[k] == 'D':
           finalx, finaly = i, k
    graph.append(z)

# 방문한 좌표를 저장할 배열
visited = [[False] * m for _ in range(n)]
queue.appendleft((startx, starty, 0))  # 시작점 추가, 거리 0으로 초기화
visited[startx][starty] = True

def out_lines(r, c):
    return 0 <= r < n and 0 <= c < m

dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# BFS 탐색
while queue:
    r, c, dist = queue.popleft()
    
    if graph[r][c] == '*':
        for dr, dc in dd:
            nr, nc = r + dr, c + dc
            if out_lines(nr, nc) and graph[nr][nc] not in ('X', 'D', '*'):
                graph[nr][nc] = '*'
                queue.append((nr, nc, '*'))
    else:
        for dr, dc in dd:
            nr, nc = r + dr, c + dc
            if out_lines(nr, nc) and not visited[nr][nc] and graph[nr][nc] != '*' and graph[nr][nc] != 'X':
                visited[nr][nc] = True
                if nr == finalx and nc == finaly:
                    print(dist + 1)
                    exit()
                queue.append((nr, nc, dist + 1))

print('KAKTUS')