import sys
input = sys.stdin.readline
arr = []
zeroArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
arr.append(zeroArr)
for i in range(1,15):
    afa =[]
    r = 0
    for k in range(14):
        r += arr[i-1][k]
        afa.append(r)
    arr.append(afa)
for i in range(int(input())):
    n = int(input())
    k = int(input())
    print(arr[n][k-1])