import math
n = int(input())
numberList = []
dic = {}
same = []
for i in range(n):
    x=int(input())
    numberList.append(x)
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] +=1    
z = sum(numberList)/n
print(round(z))
numberList.sort()
middlenum = n//2
print(numberList[middlenum])
dic = sorted(dic.items(), key = lambda x: x[1])
same.append(dic[0][0])
del dic[0]
temp =0
while True:
   try: 
    if same[0] == dic[temp][1]:
        same.append(dic[temp][0])
        temp +=1
        continue
    else:
        break
   except:
       break 
if len(same) == 1:
    print(same[0])
else:
    same.sort()
    print(same[1])        
print(abs(numberList[0])+abs(numberList[-1]))