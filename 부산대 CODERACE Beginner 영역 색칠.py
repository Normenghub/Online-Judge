a,b = map(int,input().split())

maps = []
count = 0
for _ in range(a):
    lists = list(map(int,input().split()))
    maps.append(lists)
    

for k in range(a):
    q= 0
    one = 0
    two = 0
    if maps[k][q] ==1:
        one +=1
    elif maps[k][q] ==2:
        two +=1
    else:
        pass
    q = 1
    while q < b:
        if maps[k][q] == 0:
         if maps[k][q] !=maps[k][q-1]:
            if one == two==0:
             q+=1   
             continue
            elif one >= two:
                count += 1 + two
                q +=1
                one =0
                two =0
                continue
            else:
                count += 1+ one
                q+=1
                one =0
                two =0
                continue
         else:
             q +=1
             continue
        
        
        elif maps[k][q] == 1:
          if maps[k][q] == maps[k][q-1]:
              q+=1
              continue
          else:
              one +=1
              q+=1
              continue
        else:    
          if maps[k][q] == maps[k][q-1]:
              q+=1
              continue
          else:
              two +=1
              q+=1
              continue  
    if one == two==0:
             q+=1   
             continue
    elif one >= two:
                count += 1 + two
                continue
    else:
                count += 1+ one 
                continue   
           
print(count)          
         # 1 1 0 1 1 2 2 1 2 2 1  1 1 2 2 1 1 2 2
