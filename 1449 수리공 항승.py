import sys
input = sys.stdin.readline

n , k = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
s = arr[0]
count = 0
if k != 1:

 for i in range(1,len(arr)):
    if s == 0:
        s = arr[i]
        continue
    if s - arr[i] + 1 == k:
        count += 1 
        s = 0
    elif s - arr[i] + 1 > k:
        count +=1 
        s = arr[i]
    elif s - arr[i] + 1 < k:
        continue       

else:
  print(len(arr))
  exit()
if s == arr[-1]:
   print(count+1)
elif s== 0:
   print(count)   

else:
   if s in arr:
      print(count + 1)

