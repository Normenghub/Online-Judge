import sys 
input = sys.stdin.readline
from functools import cmp_to_key
result = ''
n = int(input())
lists = list(map(str,input().rstrip().split()))
def compo(x,y):
  if x+y >= y+x:
    return -1
  else:
    return 1  
lists.sort(key=cmp_to_key(compo))
for i in lists:
  result += i
print(int(result))  
#1111111111111111110111101111101111110111111011011101010101011010101010
#1111111111111111110111101111101111110111111011011101010101011010101010