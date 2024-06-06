import sys
from collections import deque
input = sys.stdin.readline

g = int(input())
for i in range(g):
    n , k = map(int,input().split())
    x = deque(map(int,input().split()))
    save = deque()
    for kx in range(len(x)):
        save.append(kx)
    temp = 0
    while True:
        if len(x) == 0:
           break
        maxValue = max(x)
        if x[0] < maxValue:
            x.append(x.popleft())
            save.append(save.popleft())

        else:
            xx = x.popleft()
            kk = save.popleft()
            temp +=1 
            if kk == k:
                break
            else:
                continue
    print(temp)        




        
    
