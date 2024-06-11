import sys
input =sys.stdin.readline

strings = input().rstrip()
lists = []
for i in range(len(strings)):
    lists.append(strings[i:])
lists.sort()
for k in lists:
    print(k)