import sys
from collections import deque
input = sys.stdin.readline
for i in range(int(input())):
    queue =deque()
    n = int(input())
    flag = False
    dic = {}
    l = deque()
    x,y = map(int,input().split())
    dic[f'{x} {y}'] = False
    queue.append([x,y])
    for _ in range(n):
        a, b = map(int,input().split())
        dic[f'{a} {b}'] = False
        l.append([a,b])
    final_x,final_y = map(int,input().split())
    dic [f'{final_x} {final_y}'] = False
    l.append([final_x,final_y])
    def bfs(queue,dic,l,final_x,final_y,flag):
        while queue:
            r ,c  = queue.popleft()
            dic[f'{r} {c}'] = True
            leng = len(l)
            for _ in range(leng):
                q , u = l.popleft()
                if not dic[f'{q} {u}'] and (abs(r-q) + abs(c-u)) <= 1000:
                    if final_x == q and final_y == y:
                        dic [f'{final_x} {final_y}']=  True
                        flag = True
                        break
                    queue.append([q,u])
                else: l.append([q,u])
                if flag == True:
                    break
    bfs(queue,dic,l,final_x,final_y,flag)
    if dic [f'{final_x} {final_y}']:
        print('happy')
    else:
        print('sad')
    
    