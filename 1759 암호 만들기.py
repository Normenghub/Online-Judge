import sys
from itertools import combinations
input = sys.stdin.readline
n , k = map(int,input().split())
arr= list(map(str,input().split()))
arr.sort()
lists = []
for i in range(k-n+1):  
    c = str(arr[0])
    del arr[0]
    x = list(combinations(arr,n-1))
    for l in range(len(x)):
        count = 0
        if c == 'a' or c== 'e' or  c== 'i' or  c=='o' or  c== 'u':
            count = 1
            count += x[l].count('a')
            count += x[l].count('e')
            count += x[l].count('i')
            count += x[l].count('o')
            count += x[l].count('u')
        else:
            count += x[l].count('a')
            count += x[l].count('e')
            count += x[l].count('i')
            count += x[l].count('o')
            count += x[l].count('u')         
        if count >=1 and len(x[l])+1 - count >=2:
         for ll in range(len(x[l])):
            c += x[l][ll]
         lists.append(c)
         c = c[0]    
        else:
           continue
for x in lists:
   print(x)       
     