import itertools 
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = map(int,input().split())
nCr = itertools.permutations(arr,m)
nCr = list(nCr)
nCr.sort()
for z in range(len(nCr)):
    for k in range(len(nCr[z])):
        print(f"{nCr[z][k]}",end = " ")
    print()    