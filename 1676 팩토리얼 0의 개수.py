import math
import sys 
input=sys.stdin.readline
n = int(input())
s = str(math.factorial(n))
zeroCount = 0

for i in range(len(s)-1,-1,-1):
    if s[i] == '0':
        zeroCount +=1
    else:
        break
print(zeroCount)        