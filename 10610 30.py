strings = list(input())

if '0' not in strings:
    print(-1)
    exit()

else:
    sum = 0
    for i in range(len(strings)):
        sum += int(strings[i])
    if sum % 3 !=0:
            print(-1)
            exit()

    else:
            strings.sort(reverse=True)
            TEXT = ''
            for z in strings:
              TEXT += z


print(TEXT)              
