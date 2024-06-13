import sys
input = sys.stdin.readline
n = int(input())
dic = {}

for _ in range(n):
    a,b = map(str,input().split('.'))
    b = b[:-1]
    if b in dic:
        dic[b] +=1
    else:
        dic[b] = 1
lists = list(dic.keys())
print(dic)
lists.sort()
for i in lists:
    print(i,end=" ")
    print(dic[i])