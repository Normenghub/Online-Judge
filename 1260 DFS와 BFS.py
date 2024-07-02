import sys
from collections import deque
input= sys.stdin.readline
n,m,v = map(int,input().split())
dfsVisited = [False] * (n+1)
bfsVisited = [False] * (n+1)
dic = {}
arr = [[]]
for _ in range(m):
    a , b = map(int,input().split())
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]
    if b in dic:
        dic[b].append(a)
    else:
        dic[b] = [a]   
for i in range(1,n+1):
    try:
        dic[i].sort()
        arr.append(dic[i])
    except:
        arr.append([])
def dfs(arr,v,dfsVisited):
    dfsVisited[v] = True
    print(v, end = " ")
    for i in arr[v]:
        if not dfsVisited[i]:
            dfs(arr,i,dfsVisited)

def bfs(arr,v,bfsVisited):
    queue = deque([v])
    bfsVisited[v] = True
    while queue:
        dd = queue.popleft()
        print(dd, end = ' ')
        for i in arr[dd]:
            if not bfsVisited[i]:
                queue.append(i)
                bfsVisited[i] = True


dfs(arr,v,dfsVisited)
print()
bfs(arr,v,bfsVisited)
