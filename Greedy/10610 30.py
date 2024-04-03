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
# 3의 배수 판정법 0 여부에 따른 10의배수 판별후 자릿수합이 % 3==0 으로 3의배수 판별 
