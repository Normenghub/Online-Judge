import sys
from collections import deque
strings = deque(sys.stdin.readline().rstrip())
bomb = deque(sys.stdin.readline().rstrip())  
lengthBomb = len(bomb)
result = deque()
for i in strings:
    if i == bomb[-1]:
        result.append(i)
        if len(result) >= lengthBomb:
            flag = False
            temp = -1
            for k in range(len(result)-1,len(result)-lengthBomb-1,-1):
                if result[k] == bomb[temp]:
                    temp -=1
                else:
                    flag =True
                    break
            if flag == False:
               for _ in range(lengthBomb):
                   result.pop()
            else:
                pass
        else:
            pass   
    else:
        result.append(i)
if len(result) ==0:
    print("FRULA")
else:
    for x in result:
        print(x,end="")       








