import sys
import heapq
input = sys.stdin.readline
k = int(input())
def sync(arr):
    while arr and not trueFalse[arr[0][1]]:
        heapq.heappop(arr)

for _ in range(k):
    maxArr = []
    minArr = []
    arrLength = 0
    n = int(input())
    trueFalse = [False] * (n)
    for i in range(n):
        s = input().rstrip()
        if s[0] == 'I':
            heapq.heappush(maxArr,(-int(s[2:]),i))
            heapq.heappush(minArr,(int(s[2:]),i))
            trueFalse[i] = True
        else:
            if s[2:] == '1':
                sync(maxArr)
                if len(maxArr) == 0:
                    continue
                maxValue = heapq.heappop(maxArr)
                trueFalse[maxValue[1]] = False 
            else:
                sync(minArr)
                if len(minArr) == 0:
                    continue
                minValue = heapq.heappop(minArr)
                trueFalse[minValue[1]]= False
    sync(maxArr)ㅋ
    sync(minArr)
    lengh = len(maxArr)
    if lengh == 0:
        print("EMPTY")
    else:
        s = heapq.heappop(maxArr)[0]
        c = heapq.heappop(minArr)[0]
        print(f"{-s} {c}")    
                





