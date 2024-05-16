import sys

a ,b = map(int,sys.stdin.readline().rstrip().split())
packageMin = []
arr = []
result = 0
for i in range(b):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
s = []

if a>=6:
   arr.sort(key=lambda x: (x[0],x[1])) 
   d = 1001
   for k in range(len(arr)):
    if arr[k][1] < d:
       d = arr[k][1]
    result3 = d * a        
   while a > 6:
       result += arr[0][0]
       a -=6
   result1 = result
   result += (d*a)
   result1 += arr[0][0]    
   s=[result3,result1,result]
   s.sort()
   print(s[0])
else:
    arr.sort(key=lambda x: (x[1],x[0]))
    d = 1001
    for k in range(len(arr)):
     if arr[k][0] < d:
        d = arr[k][0] 
    result = a * arr[0][1]
    result1 = d 
    s=  [result,result1]
    s.sort()
    print(s[0])   
    