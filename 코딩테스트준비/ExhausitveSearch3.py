from itertools import product
import copy
count = 0
directionSpread = [0,1,2,3]
directioncombination = list(product(directionSpread, repeat = 3))
maps = []
for _ in range(5):
    lists = list(map(int,input().split()))
    maps.append(lists)

r,c = map(int,input().split())
maps[r][c] = -1
def outline(r,c): 
    return 0<=r<=4 and 0<=c<=4
savemaps = copy.deepcopy(maps)
def findDirection(maps,r,c,directioncombination,count,savemaps):

    dd = [[0,1],[0,-1],[1,0],[-1,0]]
    saver = r
    savec = c
    for i in directioncombination:
      count = 0
      r = saver
      c = savec 
      maps = copy.deepcopy(savemaps)
      for k in range(3):
          dr = dd[i[k]][0]
          dc = dd[i[k]][1]
          r += dr
          c += dc
          if outline(r,c)==False or maps[r][c]== -1:
              break
          elif outline(r,c) and maps[r][c] ==1:
              count +=1
              maps[r][c] = -1
              continue
          elif outline(r,c) and maps[r][c] ==0:
              maps[r][c]= -1
              continue

      if count ==2:
              return 1
    return 0      
          
          


print(findDirection(maps,r,c,directioncombination,count,savemaps))
