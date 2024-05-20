import sys
input = sys.stdin.readline
n,k = map(int,input().split())
numbers = list(map(int,input().split()))
s = numbers[0]
save = []
save.append(s)
for i in range(1,len(numbers)-1):
    if s != numbers[i]:
        s = numbers[i]
        save.append(s)
    else:
        continue
print(save)        