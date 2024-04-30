array = []
num1 , num2 = map(int,input().split())
for i in range(num1): 
 lists = list(map(int,input().split()))
 array.append(lists)

for i in range(num2):
   listss = list(map(int,input().split()))
   if len(listss) == 6:
     for k in range(listss[1],listss[3]+1):
       for kk in range(listss[2],listss[4]+1):
          array[k][kk] += listss[5]

   else:  
     sum = 0
     for k in range(listss[1],listss[3]+1):
       for kk in range(listss[2],listss[4]+1):
          sum += array[k][kk]  
     print(sum)