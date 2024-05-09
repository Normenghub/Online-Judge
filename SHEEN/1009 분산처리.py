n = int(input())

for i in range(n):
 c = []
 a ,b = map(int,input().split())
 if b > 1 and a !=1:
  while b<=1:
    c.append(b//2)
    b -= (b//2)
  c.append(b)
  result=0
  for i in c:
   if i * a >= 10:
     result += (a**i) % 10
   else:
     result += (a*i)
  print(result)    
 elif a ==1 and b !=1:
   print(1)
 else:
   print(0)  

  
