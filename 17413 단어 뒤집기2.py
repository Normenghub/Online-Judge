strings = input()
result = ''
save = ''
count =0
binarys = 0
for i in strings:
    if i == '<':
       count +=1
       result  += save[::-1]
       save = ''
       binarys = 1
    elif i == '>':
        binarys = 2 

    if binarys ==1:
        result +=i
    elif binarys ==2:
       result +=i    
       binarys =0
    else:
      if i ==' ':
        result  += save[::-1]
        result +=i
        save = ''
      else:  
       save+=i
result += save[::-1]       
if count >=1: 
   print(result)      
else:
   print(result)

      
