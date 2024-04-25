count = int(input())

for w in range(count):
 num = int(input())
 array = []
 for i in range(num):
  c = list(map(int,input().split()))
  array.append(c)

 array.sort()

 indexx = []
 for k in range(num-1):
  for z in range(k+1, num):
    if array[k][0] < array[z][0]:
       if array[k][1] < array[z][1]:
         
        indexx.append(z)
       else:
         pass
    else:
      continue

 indexx = list(set(indexx))

 print(len(array)-len(indexx))


