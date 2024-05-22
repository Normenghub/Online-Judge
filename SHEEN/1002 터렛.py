
n = int(input())

for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    centerDistance = ((abs(x2-x1)**2) + ((abs(y2-y1)**2)))**0.5
    
    if r2 >r1:
        more = r2
    else:
        more = r1    
    if x1== x2 and y1 == y2 and r1==r2:
        print(-1)
    elif  x1== x2 and y1 == y2 and r1!=r2:
        print(0)
    elif centerDistance > more: # 외접원
        if centerDistance == float(abs(r1+r2)):
            print(1)
        elif centerDistance < float(abs(r1+r2)):

            print(2)
        else:
            print(0)

    elif centerDistance < more:     
         #내접원
        if centerDistance == float(abs(r2-r1)):
            print(1)
        elif centerDistance < float(abs(r2-r1)):
            print(0)
        else:
            print(2)      
    else:
        print(2)



#더큰 원안에 작은 원의 중심이 있다, 원의 중심이 둘다 밖에있다.
        '''
        외접 내접 중심같음 (반지름 같음, 반지름 다름)
        중심 교집합 , 중심 독립 
        
        
        '''