import sys
input =sys.stdin.readline
arr = []
ranking = []
dic = {}
for i in range(int(input())):
    c = list(map(int,input().split()))
    arr.append(c)
for i in range(len(arr)):
   count = 0
   for k in range(len(arr)):
       if arr[i][0] <= arr[k][0] and arr[i][1] <= arr[k][1]:
           count +=1
       else:
           continue
   ranking.append(abs(count))
for i in ranking:
    print(i, end = " ")
