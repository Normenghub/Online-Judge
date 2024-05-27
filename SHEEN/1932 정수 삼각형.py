import sys
input = sys.stdin.readline
maps = []
n = int(input())
for i in range(n):
    smallList = list(map(int,input().split()))
    maps.append(smallList)
for k in range(len(maps)-2,-1,-1):
    for z in range(len(maps[k])):
        fir = maps[k+1][z] + maps[k][z]
        sec = maps[k+1][z+1] + maps[k][z]
        if fir >= sec:
            maps[k][z] = fir
        else:
            maps[k][z] = sec
print(maps[0][0])            
        