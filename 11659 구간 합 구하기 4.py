import sys
input = sys.stdin.readline
n , m = map(int,input().split())
arr = list(map(int,input().split()))
saveSum = []
sum = 0
for k in range(n):
    sum +=arr[k]
    saveSum.append(sum)   
for i in range(m):
    a, b = map(int,input().split())
    if a == b :
        print(arr[a-1])
    else:
     if a == 1:
        print(saveSum[b-1])
     else:
        print(saveSum[b-1]-saveSum[a-2])   

