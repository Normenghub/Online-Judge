import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
tree = []
n = int(input())
if n == 1:
    print(0)
    exit()
result =[]
dic = {}
tf = []
c = 0
for i in range(n+1):
    tree.append([])
    result.append(0)
    tf.append(False)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    dic[f'{a} {b}'] = c
    dic[f'{b} {a}'] = c
tf[1] = True
def dfs (tf,tree,dic,v,c,result):
    tf[v] = True
    for i in tree[v]:
        if not tf[i]:
            try:
             c=dic[f"{v} {i}"] + result[v]
             result[i] = c
            except:
             pass
            dfs(tf,tree,dic,i,c,result)
dfs(tf,tree,dic,1,c,result)
s = result.index(max(result))
tf = [False] * (n+1)
result2 = []
for i in range(n+1):
    result2.append(0)
dfs(tf,tree,dic,s,c,result2)
print(max(result2))