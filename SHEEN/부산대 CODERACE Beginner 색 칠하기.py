a, b =map(int,input().split())
maps = []
count = 0
q =0
w = 0
ccount = 0
for i in range(a):
    smallMaps = list(map(int,input().split()))
    maps.append(smallMaps)
'''

def solution(maps,w,ccount,q):
    for zz in range(len(maps)):
        q =0
        w = 0
        while q < b:
            if maps[zz][q] ==0:
                w = maps[zz][q]
                q+=1    
                continue
            else:

                if w ==maps[zz][q]:
                    w = maps[zz][q]
                    q+=1
                    continue
                else:
                
                    ccount +=1
                    w = maps[zz][q]
                    q+=1
                    continue
                    
    return ccount    

print(solution(maps,w,ccount,q))

'''


# 1 1 2 2 , 1 0 1 2, 1 1 1 0 2 2 2, 1 1 0 1 2 1 1\

# 덧칠이 가능함. 0이 나오기전까지 1 ,2가 공존하면 +2 하면되고 만약에 1, 2 하나만 존재할시 +1 하면댐 