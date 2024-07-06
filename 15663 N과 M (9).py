import sys
from itertools import permutations as sex
a ,b = map(int,input().split())
x = list(map(int,input().split()))
arr = list(sex(x,b))
arr = list (set(arr))
arr.sort()
for i in range(len(arr)):
    for k in range(len(arr[i])):
        print(arr[i][k], end =" ")
    print()
