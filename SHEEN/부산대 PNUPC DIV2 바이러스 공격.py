import sys 
input = sys.stdin.readline
from collections import deque
import copy
N,M = map(int,input().split())
Tg, Tb, X, B = map(int,input().split())
maps = []
save = deque()
save2 = deque()
nomordic={}
saveAll = {}
buildingSave = deque()
for Nc in range(N):
   strings = list(input())
   maps.append(strings)
   for elementStrings in range(len(strings)-1):
      if strings[elementStrings] == '*':
        save2.append([Nc,elementStrings])
        saveAll[f'{Nc+1} {elementStrings+1}'] = 1
      saveAll[f'{Nc+1} {elementStrings+1}'] = 1     

def outLines(r,c):
   return 0 <=r<= N-1 and 0<=c<=M-1
   
dd= [[0,1],[0,-1],[1,0],[-1,0]]
for Tgc in range(Tg):
   save = copy.deepcopy(save2)      
   for r ,c in save:
     if maps[r][c] == '*':  
       if f'{r+1} {c+1}' in saveAll:
        del saveAll[f'{r+1} {c+1}']
       for dr ,dc in dd:
          drr = dr + r
          dcc = dc + c        
          if  outLines(drr,dcc) and maps[drr][dcc] == '*':
           if f'{drr+1} {dcc+1}' in saveAll:
             del saveAll[f'{drr+1} {dcc+1}']              
           continue
          elif outLines(drr,dcc) and maps[drr][dcc] == '.':
             maps[drr][dcc] = '*'
             if f'{drr+1} {dcc+1}' in saveAll:
              del saveAll[f'{drr+1} {dcc+1}']          
             save2.append([drr,dcc])
          elif outLines(drr,dcc) and maps[drr][dcc] == '#':   
             save2.append([drr,dcc])
             maps[drr][dcc] = 'B'       
             buildingSave.append([drr,dcc,Tgc])
             pass
          else:
             continue               
     else:
        pass   
     save2.popleft()  
   if len(buildingSave) >=1: 
    for _ in range(len(buildingSave)):
       if buildingSave[0][2] == Tgc-Tb:
          maps[buildingSave[0][0]][buildingSave[0][1]]= '*'
          if f'{buildingSave[0][0]+1} {buildingSave[0][1]+1}' in saveAll:
           del saveAll[f'{buildingSave[0][0]+1} {buildingSave[0][1]+1}']
          save2.append([buildingSave[0][0],buildingSave[0][1]])
          buildingSave.popleft()
       else:
             break       

lastList = list(saveAll.keys())
if len(lastList)>=1:
 for g in lastList:
   print(g)
else:
   print(-1)   