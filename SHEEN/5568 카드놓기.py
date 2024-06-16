from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr=[]
for i in range(n):
    arr.append(input().rstrip())
x = list(permutations(arr,k))
arr = []
for k in range(len(x)):
    result = ''
    for z in range(len(x[k])):
      result += x[k][z]
    arr.append(int(result))
arr = list(set(arr))   
print(len(arr))  