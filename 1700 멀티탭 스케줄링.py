'''
belady's min algorithm Optimal page change
'''

import sys
imput = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int,input().split()))
temp = arr[0]
arr1 = [arr[0]]
for ds in range(1,len(arr)):
   if temp == arr[ds]:
      pass
   else:
      arr1.append(arr[ds])
      temp = arr[ds]
arr = arr1
count = 0
save = []
for i in range(len(arr)):
    if len(save) < n:
       save.append(arr[0])
       del arr[0]
       continue
    else:
       e = []
       for x in range(len(save)):
          temp = False
          for k in range(len(arr)):
             if save[x] == arr[k]:
                e.append(k)
                temp = True
                break
             else:
                continue
          if temp == False:
             e.append(k+1)   
       maxs = e.index(max(e))
       if arr[0] in save:
          del arr[0]
          pass
       elif save[maxs] == arr[0]:
           del arr[0]
       else:
          count +=1
          del save[maxs]
          save.append(arr[0])
          del arr[0]
      

print(count)              
                             
                       
          
          