import sys
n, m= map(int,sys.stdin.readline().rstrip().split())
x =0
for i in range(n):
 a = list(map(int,sys.stdin.readline().rstrip().split()))
 a.sort()
 if a[0] > x:
  x = a[0]
 else:
  continue
print(x)  


# min함수 사용시 복잡도 더 적음 