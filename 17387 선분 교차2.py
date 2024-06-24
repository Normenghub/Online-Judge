import sys
input = sys.stdin.readline
# 선분 1을 기준으로 외적 계산 
x1,y1,x2,y2  = map(int,input().split())
if x1>=x2:
    maxs1 =x1
    mins1 = x2
else:
    mins1 = x1
    maxs1 = x2    
if y1>=y2:
    maxy1 =y1
    miny1 = y2
else:
    miny1 = y1
    maxy1 = y2      
x3,y3,x4,y4 = map(int,input().split())
if x3>=x4:
    maxs2 = x3
    mins2 = x4
else:
    mins2 = x3
    maxs2 = x4    
if y3>=y4:
    maxy2 =y3
    miny2 = y4
else:
    miny2 = y3
    maxy2 = y4  

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)

l1 = ccw(x1,y1,x2,y2,x3,y3)
l2 = ccw(x1,y1,x2,y2,x4,y4)
l3 = ccw(x3,y3,x4,y4,x1,y1)
l4 = ccw(x3,y3,x4,y4,x2,y2) 
if l1 * l2 == 0 and l3 * l4 == 0:
   if mins1 == mins2 and maxs1 ==maxs2 and miny1 == maxy2 and maxy1 == maxy2:
       print(1)
   elif y1==y2==y3==y4:
       if (mins1 <= maxs2 and mins2 <= maxs1):
           print(1)
       else:
           print(0)
   elif x1==x2==x3==x4:
       if (miny1 <= maxy2 and miny2 <= maxy1):
           print(1)
       else:
           print(0)
   # 기울기 같을때 처리, 한 점에서 만날때 처리 
   elif (x1==x3 and y1==y3) or(x1==x4 and y1==y4) or (x2==x3 and y2==y3) or(x2==x4 and y2==y4):
       print(1)
   else:    
       if l1==l2==l3==l4 ==0:
           if (mins2 <mins1 < maxs2 and miny2 < miny1 < maxy2) or (mins1 < mins2 <maxs1 and miny1 < miny2 < maxy1):
               print(1)
           else:
               print(0)    
                                       
elif l1 * l2 <= 0 and l3 * l4 <=0:
    print(1)
else:
    print(0)    