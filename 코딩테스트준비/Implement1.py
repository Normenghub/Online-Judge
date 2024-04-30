num1, num2 = map(int, input().split())

lists = list(map(int,input().split()))
lists.sort()
for i in range(num2):
   n = int(input())
   k = 0
   for z in range(len(lists)):
    if lists[z] >= n:
      break
    else:
      k+=1  

   if len(lists)-k>0:  
            print(len(lists)-k)
   else:
             print(0)        
