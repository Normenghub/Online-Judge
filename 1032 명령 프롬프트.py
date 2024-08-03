import sys
input = sys.stdin.readline
arr = []

n = int(input())
for _ in range(n):
    arr.append(input().rstrip())
asd = len(arr[0])

if n == 1:
    print(arr[0])
    exit()

for i in range(asd):
    flag = True
    for k in range(1,len(arr)):
        if arr[k][i] == arr[k-1][i]:
            continue
        else:
            flag = False
            break
    if flag:
        print(arr[k][i],end="")
    else:
        print('?',end="")
        
