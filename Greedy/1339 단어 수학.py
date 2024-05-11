'''dic = {" " : ''}
n = int(input())
arr = []
temp = 9
arr2 = []
arr3 = []
for i in range(n):
   strings = input()
   x = 8 - len(strings) 
   strings = (' '* x) + strings
   arr.append(strings)
arr.sort(reverse=True) 
for k in range(8):
   for z in range(len(arr)-1,-1,-1):
         if arr[z][k] not in dic:
            dic[arr[z][k]] = str(temp)
            temp -=1 
            arr3.append(arr[z][k])
         else:
            continue   
for kk in range(len(arr)):
   s = ''
   for zz in range(8):
        
        if dic[arr[kk][zz]] == " ":
          continue
        else:
            s += dic[arr[kk][zz]]

   arr2.append(int(s)) 
print(arr)
print(dic)
print(sum(arr2)) 

'''
import sys
n= int(input())
dic = {}
arr = [sys.stdin.readline().strip() for _ in range(n)]
for strings in arr:
    lengths = len(strings)-1
    for k in strings:
      if k in dic:
         dic[k] += (10**lengths)
      else:
         dic[k] = (10**lengths)   
      lengths-=1
dic = sorted(dic.items(), key=lambda c : c[1], reverse=True)
sum = 0
multi = 9
for asd in range(len(dic)):
 sum += (multi*dic[asd][1])
 multi -=1
print(sum)