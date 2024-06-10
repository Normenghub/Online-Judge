import sys
n,k = map(int,sys.stdin.readline().split())
dic = {}
for _ in range(n):
    s ,b = map(str,sys.stdin.readline().split())
    dic[s] = b
for _ in range(k):
    s = sys.stdin.readline().rstrip()
    print(dic[s])    