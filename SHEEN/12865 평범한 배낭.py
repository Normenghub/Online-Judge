# bottom - up DP
import sys 
input = sys.stdin.readline
n , k = map(int,input().split())
infor = []
for _ in range(n):
    c = list(map(int,input().split()))
    infor.append(c) 
temp = 0
saveArr = []
arr =[0] * k 
for x in range(k):
    if infor[0][0] >= x+2:
        continue
    else:
        arr[x] = infor[0][1]
saveArr.append(arr)
for _ in range(n-1):
    s = [0] * k
    saveArr.append(s)

for i in range(1,n):
    for f in range(k):
        if infor[i][0]-1 > f:
            saveArr[i][f] = saveArr[i-1][f]
        elif infor[i][0]-1 == f:
            saveArr[i][f] = max(infor[i][1], saveArr[i-1][f])
        else:
            saveArr[i][f] = max(infor[i][1]+saveArr[i-1][f-infor[i][0]],saveArr[i-1][f])

       
print(saveArr[-1][-1])

            

