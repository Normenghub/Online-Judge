import sys 
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a,b,c,d = map(str,input().split())
    x = []
    x.append(a)
    x.append(int(b))
    x.append(int(c))
    x.append(int(d))
    arr.append(x)
arr.sort(key= lambda f : (-f[1], f[2], -f[3],f[0])) 
for k in range(n):
    print(arr[k][0])
