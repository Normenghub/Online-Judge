import copy
'''
import sys
input = sys.stdin.readline
import time
'''
'''
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

''' # 완전탐색 출력 초과

# 처음 좌표 저장 해놓기 

N,M = map(int,input().split())
Tg, Tb, X, B = map(int,input().split())
saveAll = []
maps = []
recentAddMaps = []
nomordic = {}
save = []
save2 = []
for qw in range(N):
    s=input()
    s=list(s)
    maps.append(s)
    for qwe in range(len(s)):
      if s[qwe] == '*':
         save.append([qw,qwe])
         save2.append([qw,qwe]) 
      else:
         saveAll.append([qw,qwe])
         continue
def NoOutLines(r,c):
    return 0<= r <= N-1 and 0<= c <= M-1
dd = [[0,1],[0,-1],[1,0],[-1,0]]

for zz in range(Tg):
   save = copy.deepcopy(save2)
   for r,c in save:
      temp = 0
      for dr,dc in dd:
         
         drr = dr+r
         dcc = dc+c
         if NoOutLines(drr,dcc):
          if maps[drr][dcc] == '.':
            maps[drr][dcc] = '*'
            if [drr,dcc] not in save2:
             save2.append([drr,dcc])
            else:
               continue
            temp +=1
            continue
          elif maps[drr][dcc] == '*':
            if [drr,dcc] not in save2:
             save2.append([drr,dcc])
            else:
               continue
            temp +=1
            continue
          elif maps[drr][dcc] == '#':
            maps[drr][dcc] = zz
            continue
          elif maps[drr][dcc] == '#':
            maps[drr][dcc] = zz
            continue
          elif isinstance(maps[drr][dcc], int):
             if maps[drr][dcc] == zz-Tb:
                  maps[drr][dcc] = '*'    
                  if [drr,dcc] not in save2:
                     save2.append([drr,dcc])
                  else:
                    continue                
                  temp +=1     
                  continue
             else:
                continue
                
         else:
            continue
      if temp ==4:
       save2.remove([r,c])
      else:
        pass
   for asd in save2:
      if asd in saveAll:
         saveAll.remove(asd)
      else:
         continue   

if len(saveAll) ==0:
   print(-1)
   exit()
else:
   for we ,wew in saveAll:
      print(f"{we+1} {wew+1}")   