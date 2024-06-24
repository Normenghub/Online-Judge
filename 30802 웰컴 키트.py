import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
t,p = map(int,input().split())
save = []
for i in arr:
    if i % t == 0:
        save.append(i//t)
    else:
        save.append((i//t)+1)
print(sum(save))
print(f'{n//p} {n%p}')            