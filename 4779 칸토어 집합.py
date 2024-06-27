
while True:
 n = int(input())    
 if n == 0:
    print('-')
    exit()
 
 else:
    try:
     s = "- -"
     arr = ['- -']
     for k in range(2,n+1):
      s = arr[0]+ " "*(3**(k-1)) +arr[0]
      arr[0] = s
    
    except:
        break

