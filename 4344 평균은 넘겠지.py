from collections import deque
n = int(input())
for i in range(n):
    c = deque(map(int,input().split()))
    z = c.popleft()
    c = list(c)
    va = sum(c)
    avg = va/len(c)
    count = 0
    for k in c:
        if k > avg:
            count +=1
        else:
            continue
    a = round(count/len(c),6)
    print(f'{a*100:.3f}%')