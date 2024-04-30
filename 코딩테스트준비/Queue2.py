from collections import deque

q = deque()
A =[]
B =[]
infordic = {}
num = int(input())

for i in range(num):
     smallInfor = list(input().split())
     if len(smallInfor) == 3:
        q.appendleft(int(smallInfor[1]))
        infordic[int(smallInfor[1])] = int(smallInfor[2])
     else:
        mi = int(q.pop())
        if infordic[mi] == int(smallInfor[1]):
            A.append(mi)
        else:
            B.append(mi)
A.sort()
B.sort()

C =list(q)
C.sort()
if len(A) > 0:
 for z in A:
    print(z,end=" ")
 print()    
else:
   pass 
if len(B)>0:
 for a in B:
    print(a,end=" ")
 print()    
else:
   pass
if len(C) == 0:
    print(None)
else:
    for f in C:
     print(f,end=" ")   
