import sys
import copy
input = sys.stdin.readline
for _ in range(int(input())):
    dic = {}
    n = int(input()) 
    arr = list(map(int,input().split()))
    arr2 = copy.deepcopy(arr)
    arr2.sort()
    for i in arr:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] =1
    MaxValue = arr2[-1]
    point = 0
    result = 0
    while True:
        if point == len(arr)-1:
            break
        if arr[point] != MaxValue:
            result += MaxValue - arr[point]
            dic[arr[point]] -=1
            point +=1
        else:
            dic[arr[point]] -=1
            while True:
                if len(arr2) == 0:
                    break
                arr2.pop()
                if len(arr2) == 0:
                    break
                MaxValue = arr2[-1]
                if dic[MaxValue] == 0:
                    continue
                else:
                    point+=1
                    break
    print(result)

