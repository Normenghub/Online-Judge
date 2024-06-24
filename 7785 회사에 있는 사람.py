import sys
input = sys.stdin.readline
num = int(input())
nomordic ={}
for i in range(num):
    lists = list(input().split())
    if lists[1] =="leave":
        del nomordic[lists[0]]
    else:
      nomordic[lists[0]] = lists[1]


s = sorted(nomordic.keys(), reverse=True)

for k in s:
    print(k)
