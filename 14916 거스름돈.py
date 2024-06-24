n = int(input())
count =0
if n ==1 or n == 3:
    print(-1)
    exit()
else:
    while True:
        if n // 5>0:
            count +=1
            n-=5
            
        elif n//5 ==0:
            break 
    while True:
     if n % 2 == 0:
        count += n//2
        break
     else:
        n+=5     
        count -=1       

print(count)           