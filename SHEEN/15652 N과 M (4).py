from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = [x for x in range(1,n+1)]
lists = list(combinations_with_replacement(arr, k))

for x in range(len(lists)):
    for i in range(k):
        print(lists[x][i], end = " ")
    print()    