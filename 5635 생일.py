lists = []
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a,b,c,d = map(str,input().split())
    x= []
    x.append(int(d))
    x.append(int(c))
    x.append(int(b))
    x.append(a)
    lists.append(x)
lists.sort()
print(lists[-1][-1])
print(lists[0][-1]) 