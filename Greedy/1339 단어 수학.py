dic = {" " : ''}
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
   for z in range(len(arr)):
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
if len(arr3) >=2:
    dic[arr3[0]] = '8'
    dic[arr3[1]] = '9'  
else:
    print(sum(arr2))  
    exit()
arr3 = []
print(dic)    
for kk in range(len(arr)):
   s = ''
   for zz in range(8):
        
        if dic[arr[kk][zz]] == " ":
          continue
        else:
            s += dic[arr[kk][zz]]

   arr3.append(int(s)) 
print(max(sum(arr3),sum(arr2)))   