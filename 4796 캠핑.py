result = 0
i=0
while True:
 i+=1
 a,b,c = map(int,input().split())
 if a+b+c ==0:
    break
 else:
   result =0
   df = c//b
   result += df  * a
   fc = c%b
   if fc >a:
     result += a
   else:
     result += fc
   print(f"Case {i}: {result}") 


