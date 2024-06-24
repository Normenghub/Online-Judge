import sys
import math
input =sys.stdin.readline
numbers=[]
dic = {}
n = int(input())
for _ in range(n):
    a= int(input())
    numbers.append(a)
    if a in dic:
        dic[a] +=1
    else:
        dic[a] =1    
numbers.sort()    
print(round(sum(numbers)/len(numbers)))
print(numbers[int(len(numbers)/2 - 0.5)])
dic = sorted(dic.items(), key=lambda x:(-x[1],x[0]))
temp = 0
howMany = dic[0][1]
for i in range(len(dic)):
    if dic[i][1] == howMany:
        temp +=1
    else:
        break
if temp >=2:
    print(dic[1][0])
else:
    print(dic[0][0])    
if n == 1:
    print(0)
else:
    if numbers[0] > 0 and numbers[-1] > 0:
        print(numbers[-1] - numbers[0])
    elif numbers[0] < 0 and numbers[-1] >0:
        print(numbers[-1] - numbers[0])
    else:
        print(abs(abs(numbers[-1]) - abs(numbers[0])) )   


 
      

    
