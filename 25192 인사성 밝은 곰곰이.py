import sys
input = sys.stdin.readline
n = int(input())
dic = {}
temp=1
sum = 0
for i in range(n):
    s= input()
    if s == "ENTER\n":
        sum+=(len(dic)-1)
        dic = {}
    if s not in dic:
        dic[s] =1
    else:
        dic[s] +=1
sum+=(len(dic))
print(sum)           
