import sys
input = sys.stdin.readline
n,k=map(int,input().split())
if k == 0:
   print(1)
   exit()
sys.setrecursionlimit(10**6)
count = 0

tf = [False] * (n+1)
queue = []
dic = {}
for i in range(1,n+1):
   dic[i] = []
for i in range(k):
   a, b = map(int,input().split())
   queue.append(a)
   queue.append(b)
   dic[a].append(b)
   dic[b].append(a)
def dfs(tf,dic,v):
   tf[v] = True
   for s in dic[v]:
      if not tf[s]:
         dfs(tf,dic,s)
while queue:
   
   a = queue.pop()
   if not tf[a]:
      dfs(tf,dic,a)
   else:
      continue
   count +=1
print(count)
      
      