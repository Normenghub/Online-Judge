import sys
input = sys.stdin.readline
from collections import deque

dic = dict()

maps = [999999] * 101

count = 0
maps[1] = 0
queue = deque()
queue.append(1)

n,m = map(int,input().split())
for _ in range(n+m): 
    a,b = map(int,input().split())
    dic[a] = b

dd = [1,2,3,4,5,6]

while queue:
    num = queue.popleft()
    for go in dd:
       togo = go + num
       if 1<=togo<=100:
        if togo in dic:
           if maps[num] + 1 <  maps[dic[togo]]: 
            maps[dic[togo]] = maps[num] + 1
            queue.append(dic[togo])
        
        elif togo not in dic:
          if maps[num] +1 < maps[togo]:
            maps[togo] = maps[num] +1
            queue.append(togo)
print(maps[100])    



