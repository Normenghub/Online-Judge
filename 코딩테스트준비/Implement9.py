# 0 land 1 sea
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
maps = []
firstLocationCount =0
directionCount = 1
r ,c , d = map(int,input().split())
for r in range(n):
    lists = list(map(int,input().split()))
    maps.append(lists)
dd = [[0,1],[1,0],[0,-1],[-1,0]]
def outLines(r ,c):
    return 0<= r <= n-1 and 0<= c <= k-1

for dr ,dc in dd:
     drr = r + dr
     dcc = c + dc
     if outLines(drr,dcc) == False or maps[drr][dcc] == 1:
        firstLocationCount +=1
     else:
        break
if firstLocationCount == 4:
     print(directionCount)
     exit()
while True:
  

        
     

print(directionCount)
