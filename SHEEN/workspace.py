from collections import deque

def find_safe_zones(N, M, T_G, T_B, X, B, grid):
    # 바이러스 전파 시뮬레이션
    virus_queue = deque()
    safe_zones = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '*':
                virus_queue.append((i, j))
            elif grid[i][j] == '#':
                safe_zones.append((i+1, j+1))

    while virus_queue:
        x, y = virus_queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#':
                if grid[nx][ny] == '.':
                    grid[nx][ny] = 'v'
                    virus_queue.append((nx, ny))
                elif grid[nx][ny] == '#':
                    for i in range(T_B):
                        for j in range(M):
                            if grid[i][j] == '#':
                                safe_zones.append((i+1, j+1))
                    for i in range(T_B, N):
                        for j in range(M):
                            if grid[i][j] == '#':
                                grid[i][j] = 'v'
                                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                    nx, ny = i + dx, j + dy
                                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '.':
                                        grid[nx][ny] = 'v'
                                        virus_queue.append((nx, ny))

    # 안전 구역 찾기
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.' or (grid[i][j] == '#' and i < T_B):
                safe_zones.append((i+1, j+1))

    if not safe_zones:
        return [-1]
    else:
        safe_zones.sort()
        return safe_zones

# 입력 받기
N, M = map(int, input().split())
T_G, T_B, X, B = map(int, input().split())
grid = [input() for _ in range(N)]

# 안전 구역 찾기
safe_zones = find_safe_zones(N, M, T_G, T_B, X, B, grid)

# 출력
for x, y in safe_zones:
    print(x, y)