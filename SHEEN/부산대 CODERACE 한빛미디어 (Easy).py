n = int(input())

arr = list(map(int,input().split()))
arr.sort()
temp = arr[0]

dic = {}
dic[arr[0]] = 1
for i in range(1,len(arr)):

 if temp*2 > arr[i]:
  dic[temp] +=1
 else:
  temp = arr[i]
  dic[temp] =1
   
print(len(dic))   