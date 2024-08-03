import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
front = [[] for _ in range(n+1)]
back = [[] for _ in range(n+1)]
people = dict()
for i in range(1,n+1): people[i] = False
sequence = []
q = deque()


for _ in range(k):
    a,b = map(int,input().split())
    front[a].append(b)
    back[b].append(a)
for i in range(1,n+1):
    if len(back[i]) == 0:
     q.append(i)
while q:
   x = q.popleft()
   people[x]= True
   sequence.append(x)
   for i in front[x]:
         flag = True
         for w in back[i]:
            if people[w]:
               continue
            else:
               flag = False
               break
         if flag:
            q.append(i)

      
for i in sequence:
   print(i,end=" ")



