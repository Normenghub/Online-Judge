from collections import deque
import sys
input = sys.stdin.readline
dic = {}
f,s,g,u,d = map(int,input().split())
tf = [-1] *(f+1)
if g == s :
   print(0)
   exit()
if g == 0 :
    print("use the stairs")
    exit()
queue = deque([s])
dd = [u,-d]
result = deque()
flag = False
leng = len(queue)
tf[s] = 0
while queue:
    x = queue.popleft()
    for c in dd:
        q = x+c
        if q == g:
           tf[q] = tf[x] + 1
           flag = True
           break
        if 0 < q<=f and tf[q] == -1:
             tf[q]= tf[x] +1
             queue.append(q)   
        else: continue     
    if flag == True:
       break

if flag == False:
   print("use the stairs")
else:
   print(tf[g])