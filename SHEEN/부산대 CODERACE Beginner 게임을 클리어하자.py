N,M = map(int,input().split())

time = 0
saveindex = 0
nomordic = {}
maps =[]
ss = 0
for i in range(N):
 lists = list(map(int,input().split()))
 maps.append(lists)
 
 
 
 
if M > 2: 
 for k in range(N):
  nomordic = {}
  index =1 
  for c in maps[k]:
   nomordic[index] = c 
   index +=1
  maps[ss].sort()
  sortednomordic = sorted(nomordic.items(), key = lambda item:item[1]) 

 
  if sortednomordic[0][0] == saveindex:
   if sortednomordic[2][1] < maps[ss+1][2]:
    saveindex = sortednomordic[2][0]
    time += sortednomordic[2][1]
   else:
    saveindex = sortednomordic[1][0]
    time += sortednomordic[1][1]  
  else:
     saveindex = sortednomordic[0][0]
     time += sortednomordic[0][1]    

  ss +=1 
else:
  for k in range(N):
   nomordic = {}
   index =1 
   for c in maps[k]:
    nomordic[index] = c 
    index +=1  
   sortednomordic = sorted(nomordic.items(), key = lambda item:item[1]) 
   if sortednomordic[0][0] == saveindex:
    saveindex = sortednomordic[1][0]
    time += sortednomordic[1][1]  
   else:
     saveindex = sortednomordic[0][0]
     time += sortednomordic[0][1]   





print(time) 

 
