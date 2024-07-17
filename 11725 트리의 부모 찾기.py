import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
tf = [False] * (n+1)
dic = {}
dic2 = {}
for _ in range(1,n+1): 
    dic[_] = []
    dic2[_] = 0
for _ in range(n-1): 
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
tf[1] = True
def dfs(tf,v):
    tf[v] = True

    for d in dic[v]:
        if not tf[d]:
            dic2[d] = v
            dfs(tf,d)
dfs(tf,1)
for i in range(2,n+1):
    print(dic2[i])