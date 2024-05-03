
A , B = map(int,input().split())
에마비 = {}
비마에 = {}
Aarr = list(map(int,input().split()))
Barr = list(map(int,input().split()))
lists = Aarr + Barr
for i in range(A):
    에마비[lists[i]] = -1
for k in range(A,len(lists)):
    if lists[k] in 에마비:
            에마비[lists[k]] +=1
    else:
          에마비[lists[k]] =2 
lists = Barr + Aarr          
for i in range(B):
    비마에[lists[i]] = -1
for k in range(B,len(lists)):
    if lists[k] in 비마에:
            비마에[lists[k]] +=1
    else:
          비마에[lists[k]] =2                   

nomordicSeason2 = {k : v for k,v in 에마비.items() if v == -1}
nomordicSeason3 = {k : v for k,v in 비마에.items() if v == -1}
print(len(nomordicSeason2) + len(nomordicSeason3))
    




