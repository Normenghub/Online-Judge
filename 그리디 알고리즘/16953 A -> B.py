#역과정 생성
A,B =input().split()
count = 1

while True:
    if int(B) <= int(A):
        break
    else:
        if B[len(B)-1] == '1':
            B = B[:-1]
            count +=1
            continue
        else: 
         if int(B) % 2 == 0:
          B = str(int(B)//2)

          
          count+=1
          continue 
         else:
          B = str(int(B)//2)
  

          print(-1) 
          exit()      



if int(B) == int(A):
    print(count)
    

else:
    print(-1)            
        
            
