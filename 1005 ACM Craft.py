import sys
from  collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    front = [[] for i in range(n+1)]
    back = [0] * (n+1)
    zeroCheck  = {}
    for i in range(1,n+1): zeroCheck[i] = True
    asd = [[] for i in range(n+1)]
    go = [-1] * (n + 1)
    sequnace = []
    save = []

    for _ in range(k):
        a, b = map(int, input().split())
        front[a].append(b)
        asd[b].append(a)
        back[b] +=1
        try:
         del zeroCheck[b]
        except:
            pass
    c = list(zeroCheck.keys())
    q = deque()
    for i in c:
        if not front[i]:
            go[i] = arr[i-1]
        else:
            q.append(i)
    while q:
        x = q.popleft()
        sequnace.append(x)
        for i in front[x]:
            back[i]-=1
            if back[i] == 0:
                q.append(i)
    for i in sequnace:
        if len(asd[i]) == 0:
                go[i] = arr[i-1]
        for z in front[i]:
            if len(asd[z]) == 1:
                
                for x in asd[z]:
                    go[z] = go[x] + arr[z-1]
                
            else:
                flag = True
                maxs = 0
                for c in asd[z]:
                    if go[c] == -1:
                        flag = False
                        break
                    else: maxs = max(maxs, go[c])
                if flag:
                    go[z] = arr[z-1] + maxs
    w = int(input())
    print(go[w])
        