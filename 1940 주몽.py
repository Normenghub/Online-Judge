import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int,input().split()))
arr.sort()
count = 0
s = arr[0]
for i in range(n-1):
 if arr[i] > m:
  break
 for k in range(i+1,n):
  if arr[i] + arr[k] > m:
   break
  else:
    if arr[i] + arr[k] == m:
     count +=1
    else:
     continue
print(count)