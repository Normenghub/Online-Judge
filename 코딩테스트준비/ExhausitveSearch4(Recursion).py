strings = input()
result = ''
while True:
    if strings[-1] == '0':
        strings = strings[:-1]
    else:
        break
for i in range(len(strings)-1,-1,-1):
    result += strings[i]


print(result)        
