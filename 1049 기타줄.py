import sys

a ,b = map(int,sys.stdin.readline().rstrip().split())
packageMin = []
arr = []
result = 0
for i in range(b):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
s = []
minPackage = 1001
minPerPrice = 1001
for dm, dv in arr:
   if minPackage > dm:
       minPackage = dm
   if minPerPrice > dv:
       minPerPrice = dv
f = a//6
ff = a% 6

s.append((f+1)*minPackage)
s.append(a*minPerPrice)
s.append((f*minPackage) + (ff*minPerPrice))
print(min(s))
    
       