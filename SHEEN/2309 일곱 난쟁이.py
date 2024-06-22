import sys
from itertools import permutations
input = sys.stdin.readline

arr= []
for i in range(9):
    arr.append(int(input()))
sumArr = sum(arr)
twoSum = list(permutations(arr,2))
for k in range(len(twoSum)):
    if twoSum[k][0] + twoSum[k][1] == sumArr-100:
        k1 = twoSum[k][0]
        k2 = twoSum[k][1]
        break
    else:
        continue
arr.remove(k1)
arr.remove(k2)    
arr.sort()
for k in range(7):
    print(arr[k])
