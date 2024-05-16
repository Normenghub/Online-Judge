import sys
n = int(sys.stdin.readline().rstrip())
maxWeight = list(map(int,sys.stdin.readline().rstrip().split()))
k = int(sys.stdin.readline().rstrip())
boxs = list(map(int,sys.stdin.readline().rstrip().split()))
result = 0
maxWeight.sort(reverse=True)
boxs.sort(reverse=True)
if boxs[0] > maxWeight[0]:
    print(-1)
    exit()
else:    
 while len(boxs) > 0 : 
  for weight in maxWeight:
    if boxs and weight < boxs[-1]:
       continue
    for box in boxs:
       if weight >= box:
           boxs.remove(box)
           break    
  result+=1      
            
print(result)    
#될 때 빼기 