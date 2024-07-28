import sys
from collections import deque
import copy
from itertools import product

# 방향 설정
directions = ['Up', 'Down', 'Right', 'Left']
ways = []

max_num = -1

# 모든 방향의 조합을 생성
for i in range(1, 6):
    elements = list(product(directions, repeat=i))
    ways.extend(elements)

# 입력 읽기
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
index = 1

arr = []
for _ in range(n):
    row = deque(int(data[index + i]) for i in range(n))
    arr.append(row)
    index += n
    for num in row:
        max_num = max(max_num, num)

# 배열 상태 보존
initial_arr = copy.deepcopy(arr)

# 게임 클래스 정의
class Game:
    @staticmethod
    def move(board, direction):
        if direction == 'Right':
            for i in range(n):
                new_row = [x for x in board[i] if x != 0]
                new_row = [0] * (n - len(new_row)) + new_row
                board[i] = deque(new_row)
        
        elif direction == 'Left':
            for i in range(n):
                new_row = [x for x in board[i] if x != 0]
                new_row = new_row + [0] * (n - len(new_row))
                board[i] = deque(new_row)
        
        elif direction == 'Up':
            for i in range(n):
                new_col = [board[k][i] for k in range(n) if board[k][i] != 0]
                new_col = new_col + [0] * (n - len(new_col))
                for k in range(n):
                    board[k][i] = new_col[k]
        
        elif direction == 'Down':
            for i in range(n):
                new_col = [board[k][i] for k in range(n) if board[k][i] != 0]
                new_col = [0] * (n - len(new_col)) + new_col
                for k in range(n):
                    board[k][i] = new_col[k]

    @staticmethod
    def merge(board, direction):
        if direction == 'Right':
            for i in range(n):
                for k in range(n-1, 0, -1):
                    if board[i][k] != 0 and board[i][k] == board[i][k - 1]:
                        board[i][k] *= 2
                        board[i][k - 1] = 0
                Game.move(board, 'Right')
        
        elif direction == 'Left':
            for i in range(n):
                for k in range(n-1):
                    if board[i][k] != 0 and board[i][k] == board[i][k + 1]:
                        board[i][k] *= 2
                        board[i][k + 1] = 0
                Game.move(board, 'Left')
        
        elif direction == 'Up':
            for i in range(n):
                for k in range(n-1):
                    if board[k][i] != 0 and board[k][i] == board[k + 1][i]:
                        board[k][i] *= 2
                        board[k + 1][i] = 0
                Game.move(board, 'Up')
        
        elif direction == 'Down':
            for i in range(n):
                for k in range(n-1, 0, -1):
                    if board[k][i] != 0 and board[k][i] == board[k - 1][i]:
                        board[k][i] *= 2
                        board[k - 1][i] = 0
                Game.move(board, 'Down')

# 모든 방향의 조합을 시도
for way in ways:
    arr = copy.deepcopy(initial_arr)
    for direction in way:
        Game.move(arr, direction)
        Game.merge(arr, direction)
    
    # 최대 값 갱신
    for row in arr:
        for value in row:
            max_num = max(max_num, value)

print(max_num)