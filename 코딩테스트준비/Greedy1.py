import sys
n,m,k = map(int,sys.stdin.readline().rstrip().split())
result = 0
arr = list(map(int,sys.stdin.readline().rstrip().split()))

arr.sort(reverse=True)

while m >0:
    for z in range(k):
        result +=arr[0]
        m -=1
        if m == 0:
         break
    if m == 0:
        break
    result += arr[1]
    
    m-=1  
print(result)