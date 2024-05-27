import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(int,input().split()))
arr.sort()
arr = list(set(arr))
if n == k:
    print(0)
    exit()
else:
    print(arr)    