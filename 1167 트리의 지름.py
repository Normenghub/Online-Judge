import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
result = [0] * (n+1)
dic= {}
queue = {}
c= 0
for i in range(n):
    s = deque(map(int,input().split()))
    x = s.popleft()
    queue[x] = [] 
    s.pop()
    for k in range(0,len(s),2):
        dic[f'{x} {s[k]}'] = s[k+1]
        queue[x].append(s[k])
tf = [False] * (n+1)
def dfs(tf,dic,v,queue,c):
    tf[v] = True
    for i in queue[v]:
        if not tf[i]:
            c = result[v] + dic[f'{v} {i}']
            result[i] = c
            dfs(tf,dic,i,queue,c)
dfs(tf,dic,1,queue,c)
res = result.index(max(result))
c = 0
result =[0] * (n+1)
tf = [False] * (n+1)
dfs(tf,dic,res,queue,c)
print(max(result))




