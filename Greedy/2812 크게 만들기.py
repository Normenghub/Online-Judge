import sys 

n,k = map(int,sys.stdin.readline().rstrip().split())
lens = n-k
strings = sys.stdin.readline().rstrip()
arr = []

for st in strings:
    while arr and 0< k:
      if arr[-1] < st:
         arr.pop()
         k-= 1
      else:
         break
    
    arr.append(st)     



if len(arr) == lens:
 print("".join(arr))
else:
   arr = "".join(arr)
   arr = arr[:-(len(arr)-lens)]
   print(arr)
#