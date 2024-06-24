num = int(input())
save = list(map(int,input().split()))
save.sort()

answer = 0
result = 0
for u in save:
     answer += u
     result += answer

print(result)     