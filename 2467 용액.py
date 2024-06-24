import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 1000000000000
x = 0
y = 0
start = 0
end = n-1
while start < end:
    summ = arr[start] + arr[end]
    if abs(summ) <= result:
      x = arr[start]
      y = arr[end]
      result = abs(summ)
    
    if summ < 0:
       start +=1
    
    else:
       end -=1
print(f"{x} {y}")