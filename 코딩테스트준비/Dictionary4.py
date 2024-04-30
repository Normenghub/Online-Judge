n =int(input())

nomordic = {}

array = list(input().split())

for k in array:
    if int(k) in nomordic:
        nomordic[int(k)] +=1
    else:
        nomordic[int(k)] =1
nomordic2 = dict(sorted(nomordic.items(), key = lambda x: x[1], reverse=True))
realarray = list(nomordic2.keys())
num = nomordic2[realarray[0]]
re= []
re.append(realarray[0])
del realarray[0]
for i in realarray:
   if num == nomordic2[i]:
       re.append(i)
   else:
       break    
re.sort()   

for a in re: 
    print(f"{a}", end  =" ")  