a , b= map(int,input().split())

arr = []
count =1
for i in range(a):
  w = list(map(int,input().split()))
  arr.append(w)

for k in range(a):
   f = arr[k][0]
   for z in range(1,b):
       if arr[k][z] == f:
          continue
       else:
          count +=1
          f == arr[k][z]



print(count)         
