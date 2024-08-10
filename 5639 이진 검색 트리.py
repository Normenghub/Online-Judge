import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

def postorder(s,e):
    if s > e:
        return
    mid = e + 1
    for i in range(s + 1 , e + 1):
        if arr[i] > arr[s]:
            mid = i
            break
    postorder(s + 1, mid - 1)
    postorder(mid, e)
    print(arr[s])



postorder(0,len(arr)-1)