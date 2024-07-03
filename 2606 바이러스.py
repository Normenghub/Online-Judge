import sys
sys.setrecursionlimit(10**6)
input =sys.stdin.readline
dic = {}
count =0
trueFalse = []
for i in range(int(input())+1):
    dic[i] = []
    trueFalse.append(False)
for c in range(int(input())):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
def dfs(trueFalse,dic,v):
    global count
    trueFalse[v] =True
    for i in dic[v]:
        if not trueFalse[i]:
            count +=1
            dfs(trueFalse,dic,i)
dfs(trueFalse,dic,1)
print(count)