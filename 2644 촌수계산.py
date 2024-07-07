import sys
sys.setrecursionlimit(50000000)
input = sys.stdin.readline
sys 
n = int(input())
if n == 1:
    print(-1)
    exit()
rootNode, destinationNode = map(int,input().split())
k = int(input())
tree = []
for _ in range(101):
    tree.append([])
for _ in range(k):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
tf= []
tf = [-1] * 101
tf[rootNode] = 0
def dfs(rootNode,tree,tf):
    for x in tree[rootNode]:
        if tf[x] == -1:
            tf[x] = tf[rootNode] + 1
            dfs(x,tree,tf)
dfs(rootNode,tree,tf)
print(tf[destinationNode])