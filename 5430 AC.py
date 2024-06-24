import sys 
from collections import deque
n = int(sys.stdin.readline())
for _ in range(n):
    lists = deque()
    errorCheck = False
    intstrings = ""
    rCount = 0
    sequance = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())
    arr = input()
    if len(arr)-2 == 0:
       pass
    else: 
     arr= arr[1:-1]
     for elements in arr:
        if elements == ",":
            lists.append(int(intstrings))
            intstrings = ""
            continue
        else:
         intstrings += elements 
     lists.append(int(intstrings))           
    for s in sequance:
       if s == 'R':
          rCount +=1
       else:
          try:
             if rCount % 2 == 0:
                lists.popleft()
             else:
                lists.pop()   


          except:      
                 errorCheck = True
                 break
    if errorCheck == True:
       print('error')
    else:
      if rCount %2 ==0: 
       result = '['
       if len(lists) > 0:
        result += str(lists[0])
        for w in range(1,len(lists)):
          result += ','
          result += str(lists[w])
       else:
          pass   
       result +=']'
       print(result)  
      else:
         result = '['
         if len(lists) > 0:
          result += str(lists[-1])
          for w in range(len(lists)-2,-1,-1):
            result+= ','
            result +=str(lists[w])
         else:
            pass    
         result+=']'
         print(result)

             
    
    
                
