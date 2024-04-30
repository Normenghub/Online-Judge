A = list(input().split())

B = input()
nomordic = {}

for i in A:
   for z in range(len(i)-1):
      if i[:z+1] in nomordic:
        nomordic[i[:z+1]] +=1
      else:
            nomordic[i[:z+1]] =1 



try:
 print(nomordic[B])
except:
 print(0) 
