import math
n = int(input())

for i in range(n):
     a,b = map(int,input().split())
     c = math.factorial(b)//(math.factorial(b-a)*math.factorial(1))
        
     print(c)      




