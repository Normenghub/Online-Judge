import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
count = 0
arr.sort()
while True:
    zeroCount = 0
    oddIndex =[]
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroCount +=1
            continue   
        if arr[i] % 2 != 0 :
           oddIndex.append(i)
    if zeroCount == len(arr):
       print(count)
       exit()       
    if len(oddIndex) > 0:  
     for x in oddIndex:
       arr[x] -=1
       count +=1
    else:
     for k in range(len(arr)):
        arr[k] //=2
     count +=1                 