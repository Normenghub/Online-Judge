import sys
input = sys.stdin.readline
N, M = map(int,input().split())
strings = {}
arr = []
for i in range(N):
   stringss = input()
   strings[stringss] = i

for k in range(M):
   s = input()
   if s in strings:
      arr.append(s)
   else:
      continue


print(len(arr))      