import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result =arr[0]

if arr[0] >1:
    print(1)
    exit()
else:
   temp = 0
   for i in range(1,len(arr)-1):
         result +=arr[i]
         if result < arr[i+1]-1:
             break
         else:
             temp+=1
             continue
if temp +2 == n:
    print(result+1+arr[-1])
else:
    print(result+1)




# 1 