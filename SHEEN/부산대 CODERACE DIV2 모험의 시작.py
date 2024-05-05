num = int(input())
a ,b = map(int,input().split())
temp = 0

for i in range(num):
    c,d = map(int,input().split())
    if c <= a and b < d:
        temp = 1
    else:
        continue    

if temp ==1:
    print("YES")
else:
    print("NO")    