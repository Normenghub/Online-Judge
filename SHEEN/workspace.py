import sys
input = sys.stdin.readline
from collections import deque
temp =0
N,M = map(int,input().split())
Tg, Tb, X, B = map(int,input().split())
maps = []
save = deque()
nomordic={}
lenn = 0
buildingSave = deque()
for Nc in range(N):
   strings = list(input())
   maps.append(strings)
   for elementStrings in range(len(strings)-1):
      if strings[elementStrings] == '*':
        save.append([Nc,elementStrings])
        temp+=1    
def outLines(r,c):
   return 0 <=r<= N-1 and 0<=c<=M-1 
dd= [[0,1],[0,-1],[1,0],[-1,0]]      
for Tgc in range(Tg):
   lenn =temp
   temp = 0
   for k in range(0, lenn):
      if maps[save[k][0]][save[k][1]] == '*':
         for dr,dc in dd:
            drr = save[k][0] + dr
            dcc = save[k][1] + dc
            if  outLines(drr,dcc) and maps[drr][dcc] == '*':           
              continue
            elif outLines(drr,dcc) and maps[drr][dcc] == '.':
             maps[drr][dcc] = '*'        
             save.append([drr,dcc])
             temp +=1
            elif outLines(drr,dcc) and maps[drr][dcc] == '#':   
             maps[drr][dcc] = 'B'       
             buildingSave.append([drr,dcc,Tgc])
            else:
               continue               
      else:
        pass  
                         
   if len(buildingSave) >=1: 
    for _ in range(len(buildingSave)):
       if buildingSave[0][2] == Tgc-Tb:
          maps[buildingSave[0][0]][buildingSave[0][1]]= '*'
          save.append([buildingSave[0][0],buildingSave[0][1]])
          temp +=1
          buildingSave.popleft()
       else:
             break    
   for dwa in range(lenn):
     save.popleft()  

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