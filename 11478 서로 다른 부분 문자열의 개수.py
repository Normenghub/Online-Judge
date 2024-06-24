strings = input()

nomordic = {}
plus = 0
for i in range(1,len(strings)+1):
  p = 0
  while p+i <= len(strings):
    if strings[p:p+i] in nomordic:
      nomordic[strings[p:p+i]] += 1
    else:
       nomordic[strings[p:p+i]] = 1
    p+=1   
print(len(nomordic))
    