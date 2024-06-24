import sys 
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
savearr = []
x = int(input())
dic = {}
for i in arr:
    if i>= x:
        continue
    else:
        dic[i] = 1
        savearr.append(i)
count = 0 
for k in savearr:
    dic[k] = 0
    if x-k in dic and dic[x-k] == 1:
        count +=1
        dic[x-k] = 0
    else:
        continue
print(count)
