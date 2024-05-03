import sys
input = sys.stdin.readline
nomordic ={}
a, b = map(int,input().split())

for i in range(a+b):
    s = input()
    if s in nomordic:
        nomordic[s] +=1
    else:
        nomordic[s] =1

nomordicSeason2 = {k : v for k,v in nomordic.items() if v != 1}

print(len(nomordicSeason2))

lists = sorted(nomordicSeason2.keys())
lists.sort()
for k in lists:
    print(k, end = "")