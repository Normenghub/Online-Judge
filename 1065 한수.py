import sys
input = sys.stdin.readline
n = int(input())
count =0
for i in range(1, n+1):
 if i <100:
  count +=1
 else:
  c = str(i)
  arr = []
  for k in range(len(c)-1):
   arr.append(int(c[k+1]) - int(c[k]))
  a = arr[0]
  f = False
  for z in arr:
   if z == a:
    continue
   else:
    f = True
    break
  if f == True:
   continue
  else:
   count+=1
   continue
print(count)