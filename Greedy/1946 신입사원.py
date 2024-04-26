count = int(input())
ccount =0
for w in range(count):
 num = int(input())
 array = []
 for i in range(num):
  c = list(map(int,input().split()))
  array.append(c)

 array.sort()
 
 for ii in range(len(array)):
  for iii in range(len(array)-1, ii+1,-1):
     if array[ii][1] < array[iii][1]:
       del array[iii]
       ccount +=1
 print(ccount)       
