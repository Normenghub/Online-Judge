import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline
dic = dict()
arr =[]
tfdic = {}
ara = []
n,m = map(int,input().split())

count = 0 
tf =  [False] * (n+1) 

truePeople = deque(map(int,input().split()))
truePeople.popleft()


for i in truePeople:
    tfdic[i] = True

for i in range(1,n+1): dic[i] = []

for i in range(m):
    partyPeople = deque(map(int,input().split()))
    ara.append(partyPeople)
    partyPeople.popleft()
    v = list(permutations(partyPeople,2))
    for w , c in v:
        dic[w].append(c)
        dic[c].append(w)

if len(truePeople) == 0 :
    print(len(ara))
    exit()

for i in range(1,n+1):
    dic[i] = list(set(dic[i]))

def dfs(tf,dic,v):
    tf[v] = True
    for f in dic[v]:
            if not tf[f]:
             dfs(tf,dic,f)

while truePeople:
    x = truePeople.popleft()
    if tf[x]:
        continue
    else:
        dfs(tf,dic,x)

        
for i in range(len(ara)):
        flag = True
        for k in range(len(ara[i])):
         if not tf[ara[i][k]]:
             continue
         else:
             flag = False
             break
        if flag:
            count +=1
print(count)

