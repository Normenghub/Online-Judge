strings = input()
minustrings = strings.replace('+',' ')
minustrings = minustrings.replace('-',' -')

numarr = list(minustrings.split(" "))
count = 0

     

for i in range(len(numarr)):
    if int(numarr[i])>0:
        count +=int(numarr[i])
    else:
        count +=int(numarr[i])
        break

for k in range(i+1, len(numarr)):
    count += abs(int(numarr[k])) * -1


print(count)