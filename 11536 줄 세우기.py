import sys
import copy
input = sys.stdin.readline
arr = []
arr2 = []
arr3 = []
n= int(input())
for _ in range(n):
    a = input().rstrip()
    arr.append(a)
arr2 = copy.deepcopy(arr)   
arr3 = copy.deepcopy(arr)
arr2.sort()
arr3.sort(reverse=True)
flag = True
for i in range(n):
    if arr[i] == arr2[i]:
        continue
    else:
        flag = False
        break
if flag == False:
    pass
else:
    print('INCREASING')
    exit()
flag = True        
for i in range(n):
    if arr[i] == arr3[i]:
        continue
    else:
        flag = False
        break
if flag == False:
    pass
else:
    print('DECREASING')
    exit()

print('NEITHER')


