import sys
input = sys.stdin.readline
arr = list(map(int,input().split()))
arr.sort()
for k in arr:
    print(k,end=" ")