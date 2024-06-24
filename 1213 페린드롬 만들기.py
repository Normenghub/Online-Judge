strings = input()
dic = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,}
odd = 0
lists = []
result = ""
centermemo = ""
for i in strings:
    dic[i] +=1


for z in dic:
    if dic[z] % 2 != 0 and dic[z] != 0:
        odd +=1
    elif dic[z] == 0:
        lists.append(z)
        continue

if odd >1:
    print("I'm Sorry Hansoo")
    exit()
else:
    for s in lists:
        del dic[s]
for asd in dic:
   if dic[asd] % 2 !=0:
       result += (asd *(dic[asd]//2))
       centermemo += asd
   else:
       result += (asd *(dic[asd]//2))    
reverseresult = result[::-1]
if len(centermemo) > 0:
    print(result + centermemo + reverseresult)
else:
    print(result + reverseresult)    