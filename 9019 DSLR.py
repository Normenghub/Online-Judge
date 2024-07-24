import sys
from collections import deque

input = sys.stdin.readline

class DSLR:
    @staticmethod
    def D(num):
        num = (num * 2) % 10000
        return num

    @staticmethod
    def S(num):
        num = (num - 1) % 10000
        return num

    @staticmethod
    def L(num):
        return (num % 1000) * 10 + num // 1000

    @staticmethod
    def R(num):
        return (num % 10) * 1000 + num // 10

def checkTf(tf, v, method, popNum, queue):
    if tf[v] is None:
        tf[v] = tf[popNum] + method
        queue.append(v)

def bfs(start, end):
    queue = deque([start])
    tf = [None] * 10000
    tf[start] = ''

    while queue:
        popNum = queue.popleft()

        if popNum == end:
            return tf[end]

        checkTf(tf, DSLR.D(popNum), 'D', popNum, queue)
        checkTf(tf, DSLR.S(popNum), 'S', popNum, queue)
        checkTf(tf, DSLR.L(popNum), 'L', popNum, queue)
        checkTf(tf, DSLR.R(popNum), 'R', popNum, queue)

    return None

for _ in range(int(input())):
    start, end = map(int, input().split())
    result = bfs(start, end)
    print(result)