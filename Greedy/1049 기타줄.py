import sys

a ,b = map(int,sys.stdin.readline().rstrip().split())

arr = []
for i in range(b):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

arr.sort(key=lambda x: (x[-1],x[1]))
print(arr)
