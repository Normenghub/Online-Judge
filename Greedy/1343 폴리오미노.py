import sys 
strings = sys.stdin.readline().rstrip()
saveStrings = ""
resultStrings = ""
A = "AAAA"
B = "BB"
for s in strings:
    if s =='.':
        if len(saveStrings)==0: 
            resultStrings += '.'
            continue
        else:
            if len(saveStrings) % 4 == 0 or len(saveStrings) % 2 ==0:
                 lens = len(saveStrings)
                 As = lens // 4
                 lens -= (As * 4)
                 Bs = lens//2
                 resultStrings += A * As
                 resultStrings += B * Bs
                 saveStrings = ""
                 resultStrings +='.'
            else:
               print(-1) 
               exit()
        
    else:
        saveStrings += s

if len(saveStrings) > 0:
             if len(saveStrings) % 4 == 0 or len(saveStrings) % 2 ==0:
                 lens = len(saveStrings)
                 As = lens // 4
                 lens -= (As * 4)
                 Bs = lens//2
                 resultStrings += A * As
                 resultStrings += B * Bs
                 saveStrings = ""
             else:
               print(-1) 
               exit()  
print(resultStrings)                        