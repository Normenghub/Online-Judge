import sys
N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append([int(x) for x in sys.stdin.readline().split()])

for z in range(N-1):
    index = arr[z].index(min(arr[z]))
    addindex = arr[z][index]
    del arr[z][index]
    index2 = arr[z].index(min(arr[z]))
    addindex2 = arr[z][index2]
    for zz in range(M):
        if zz == index:
          arr[z+1][zz] = arr[z+1][zz] + addindex2
        else:
            arr[z+1][zz] = arr[z+1][zz] + addindex   

print(min(arr[N-1]))             
# DP TOP DOWN , overlapping MEMOIJATION


