import sys
dic  = {}
input = sys.stdin.readline
for i in range(int(input())):
    strings = input().rstrip()
    if strings not in dic:
        dic[strings] =1
    else:
        dic[strings] +=1
dic = sorted(dic.items(), key = lambda item : (-item[1], item[0]))
print(dic[0][0])       