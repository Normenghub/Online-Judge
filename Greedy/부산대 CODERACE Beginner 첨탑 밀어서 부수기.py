num = int(input())

top = list(map(int, input().split()))
count =1
for i in range(num-1):
    if top[i] <= top[i+1]:
        count +=1

print(count)        