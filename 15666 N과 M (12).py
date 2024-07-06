from itertools import  combinations_with_replacement as sex
a,b = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
dic = {}
arr = list(sex(x,b))
arr.sort()
for i in range(len(arr)):
     if f'{arr[i]}' not in dic:
          dic[f'{arr[i]}'] = True
          for k in arr[i]:
               print(k, end = " ")
          print()
     else:
          pass
          
          
