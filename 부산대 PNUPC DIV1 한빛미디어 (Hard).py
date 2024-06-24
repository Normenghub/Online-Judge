import sys 
n = int(sys.stdin.readline().rstrip())
dic = {}
lisdic = {}
count = 0
index = 1
strings = sys.stdin.readline().rstrip()
if strings[0] =='1':
 dic[strings[2:]] = [index]
 currentPrice = int(strings[2:])
 lisdic[index] = [strings[2:]]
 count+=1
elif strings[0] =='2':
   pass
else:
   print(count)  
for i in range(n-1):
    strings = sys.stdin.readline().rstrip()
    if strings[0] == '1':
        if int(strings[2:]) >= currentPrice * 2:
            count +=1
            index +=1
            if strings[2:] not in dic:
                dic[strings[2:]] = [index]
            else:
                dic[strings[2:]].append(index) 
            lisdic[index] = [strings[2:]]    
        else:
            if strings[2:] not in dic:
                dic[strings[2:]] = [index]
            else:
                dic[strings[2:]].append(index) 
            lisdic[index].append(strings[2:])
        currentPrice = int(strings[2:])      
    elif strings[0] == '2':
       if strings[2:] in dic: 
        minindex = 2147483647
        resultIndex = 2147483647
        for st in dic[strings[2:]]:
            if len(lisdic[st]) <= minindex:
                minindex = len(lisdic[st])
                resultIndex = st
        if len(lisdic[resultIndex]) ==1:        
         del lisdic[resultIndex]
         count -=1
         del dic[strings[2:]]

        else:
           lisdic[resultIndex].remove(strings[2:])
           dic[strings[2:]].remove(resultIndex)
       else:
          pass
    else:
       print(count)   
print(dic)
print(lisdic)
       

'''
고려 해야할 것
일단 들어오는거 dic 딕셔너리에 저장 
currentPirce로 현재 가격 저장




1 1000   1 
1 4000   2
1 1000   2
1 2000   2
1 20000  3 
1 1000   3
1 4000   4
1 2000   4
2 1000   
2 1000   
2 1000  
2 1000
'''