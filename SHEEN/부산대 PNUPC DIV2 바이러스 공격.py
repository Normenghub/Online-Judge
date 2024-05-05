import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Tg, Tb, X, B = map(int,input().split())
maps = []
recentAddMaps = []
nomordic = {}
for _ in range(N):
    s=input()
    s=list(s)
    maps.append(s)   

def NoOutLines(r,c):
    return 0<= r <= N-1 and 0<= c <= M-1
dd = [[0,1],[0,-1],[1,0],[-1,0]]
for z in range(Tg):
  recentAddMaps = []
  for i in range(N):
    
    for k in range(M):
        if maps[i][k] =='.':
            continue
            
        elif maps[i][k] == '#':
           continue
           
        elif maps[i][k] == '*' and [i,k] not in recentAddMaps:
            for dr,dc in dd:
               if NoOutLines(i+dr,k+dc) == False:
                  continue
               elif NoOutLines(i+dr,k+dc) and maps[i+dr][k+dc] == '.':
                   maps[i+dr][k+dc] ='*'
                   recentAddMaps.append([i+dr,k+dc])
                   continue
               elif NoOutLines(i+dr,k+dc) and maps[i+dr][k+dc] == '#':
                  maps[i+dr][k+dc]=z
                  recentAddMaps.append([i+dr,k+dc])                 
                  continue
               else:
                  continue
        elif maps[i][k] == '*' and [i,k] in recentAddMaps:
           continue  
        elif maps[i][k] == z-Tb and [i,k] not in recentAddMaps:
           maps[i][k] = '*'
           continue
        


for q in range(N):
   for qq in range(M):
      if maps[q][qq] == '*':
         continue
      else:
         nomordic[f'{q+1} {qq+1}'] =1

if len(nomordic) == 0:
   print(-1)
else:
   nomordic = sorted(nomordic)
   for zzz in nomordic:
      print(zzz)


                             
                    