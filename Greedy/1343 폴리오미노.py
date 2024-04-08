strings = input()
save = []
count = 0
sstrings = ''
z = 0
if strings.count('X') % 4 == 0 or strings.count('X') % 2 == 0:
 for i in range(len(strings)):
    if strings[i] =='.':
       save.append(count)
       count = 0
       continue
    else:
       count+=1 
       continue
 save.append(count)  
 if 0 in save:
     save.remove(0)
 print(save)
  
   
else:
    print(-1)
    exit()
