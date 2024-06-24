import sys
input = sys.stdin.readline
dic={}
arr = []
n,k = map(int,input().split())
for i in range(n):
    team = input().rstrip()
    dic[team] = []
    dic[i] = [team]
    x = int(input())
    for _ in  range(x):
        member = input().rstrip()
        dic[team].append(member)
        dic[i].append(member)
    dic[team].sort()    
for _ in range(k):
    who = input().rstrip()
    binary = int(input())
    if binary == 0:
        for k in dic[who]:
            print(k)
        continue
    else:
        for w in range(len(dic)//2):
            if who in dic[w]:
                print(dic[w][0])
                break
            else:
                continue

        continue



