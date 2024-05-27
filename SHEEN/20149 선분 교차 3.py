import sys
input = sys.stdin.readline
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
def grid(x1,x2,x3,x4,y1,y2,y3,y4): # 기울기로 서로다를때 ( ㅣ 제외) 판정 함수 
           l1 = (y2-y1)/(x2-x1)
           l2 = (y4-y3)/(x4-x3)
           b1 = y1 - (l1 * x1)
           b2 = y3 - (l2 * x3)

           targetx = round((b2-b1)/(l1-l2),10)
           targety = round((l1 * targetx) + b1,10)
           if mins1 <= targetx and targetx <= maxs1 and miny1 <= targety and targety<= maxy1 and mins2 <= targetx and targetx<= maxs2 and miny2<= targety  and targety<= maxy2:
             return print(f'1\n{targetx} {targety}')
           else:
               return print(0)       
if x2-x1 == 0 and x4-x3 == 0:
   if x1==x2==x3==x4: 
    if miny1<miny2<maxy1 or miny1<maxy2<maxy1 or miny2< miny1 < maxy2 or miny2 < maxy1 < maxy2:
        print(1)
    elif miny2 == maxy1:
        print(1)
        print(f"{x1} {miny2}")
    elif miny1 == maxy2:
        print(1)
        print(f"{x1} {miny1}")
    elif x1==x3 and x2==x4 and y1 ==y3 and y2==y4:
       print(1)    
    else:
        print(0)
   else:

        print(0)
elif x2-x1 == 0 and x4-x3 !=0:
   l2 = (y4-y3)/(x4-x3)
   b2 = y3 - (l2 * x3)
   targety = round((l2*x1) + b2,9)
   if miny1 <= targety and targety <= maxy1 and x3<=x1<=x4:
       print(1)
       print(f'{x1} {targety}')
   else:
       print(0)    
elif x4-x3 == 0 and x2-x1 !=0:
   l1 = (y2-y1)/(x2-x1)
   b1 = y2 - (l1 * x2)
   targety = round((l1*x3) + b1,9)
   if miny2 <= targety and targety <= maxy2 and  x1 <= x3 <= x2:
       print(1)
       print(f'{x3} {targety}')
   else:
       print(0)  
else:
 if (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3): # 기울기가 같을때 
    if y1 == y2 ==y3 ==y4:
        if mins1<mins2<maxs1 or mins1<maxs2<maxs1 or mins2< mins1 < maxs2 or mins2 < maxs1 < maxs2:
            print(1)
        elif mins2 == maxs1:
           print(1)
           print(f"{mins2} {y1}")
        elif mins1 == maxs2:
           print(1)
           print(f"{mins1} {y1}")
        elif x1==x3 and x2==x4 and y1 ==y3 and y2==y4:
         print(1)     
        else:
            print(0)   
    elif x1==x3 and x2==x4 and y1 ==y3 and y2==y4:
       print(1)                
    else:
        if mins1 == maxs2:
            print(1)
            if mins1 == x1:
                print(f'{mins1} {y1}')
            else:
                print(f'{mins1} {y2}')    
        elif maxs1 == mins2:
            print(1)
            if maxs1 == x1:
                print(f'{maxs1} {y1}')
            else:
                print(f'{maxs1} {y2}')    
        elif mins2 < mins1 < maxs2 or mins1 < mins2 <maxs1 or mins2 < maxs1<maxs2 or mins1 < maxs2 <maxs1:
           l1 = (y2-y1)/(x2-x1)
           l2 = (y4-y3)/(x4-x3)
           b1 = y1 - (l1 * x1)
           b2 = y3 - (l2 * x3)
           if b1 ==b2:
               print(1)
           else:
               print(0)    
        elif mins1==mins2 and miny1 ==miny2 and maxs1 ==maxs2 and maxy1==maxy2:
            print(1)        
        else:
            print(0)
 else: # 기울기가 다를때 
        grid(x1,x2,x3,x4,y1,y2,y3,y4)
     
