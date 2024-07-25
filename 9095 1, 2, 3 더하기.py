import sys
from itertools import product
input = sys.stdin.readline

dic = {}

for i in range(1,12):
    ar = list(product(range(1,4),repeat = i))
    for k in range(len(ar)):
        if sum(ar[k]) not in dic:
            dic[sum(ar[k])] = 1
        else:
            dic[sum(ar[k])] +=1

for i in range(int(input())):
    print(dic[int(input())])