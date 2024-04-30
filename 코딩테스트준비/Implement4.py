num1 , num2 = map(int,input().split())
lists = list(map(int,input().split()))

for i in range(num2):
   smallList = list(map(int,input().split()))
   if len(smallList) == 3:
      sum = 0
      for k in range(smallList[1],smallList[2]+1):
         sum += lists[k]
      print(sum)
   else:
      for z in range(smallList[1],smallList[2]+1):
            lists[z] += smallList[3]
            
