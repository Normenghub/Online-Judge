import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dic = {}
distance = {}
def dicCheck(dic,q,w):
    if q in dic:
        dic[q].append(w)
    else:
        dic[q] = [w]


n,m = map(int,input().split())

tf = [False] * (n+1)

def dfs(tf, dic, v, q, treeDistance):
    tf[v] = True
    treeDistance += f' {v}'
    
    if v == q:
        return treeDistance.strip()
    
    for i in dic[v]:
        if not tf[i]:
            result = dfs(tf, dic, i, q, treeDistance)
            if result is not None:
                return result
            


for _ in range(n-1):
    a,b,c = map(int,input().split())
    distance[f'{a} {b}'] = c
    distance[f'{b} {a}'] = c
    
    dicCheck(dic,a,b)
    dicCheck(dic,b,a)

for _ in range(m):
    count = 0
    treeDistance = ''
    p,o = map(int,input().split())
    result = list(dfs(tf,dic,p,o,treeDistance).split())
    for i in range(len(result)-1):
        count += distance[f'{result[i]} {result[i+1]}']
    print(count)
    
    tf = [False] * (n+1)