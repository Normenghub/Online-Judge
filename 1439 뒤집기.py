# 1,0 카운트 시작 카운트 한 두 변수 리스트 저장후 최솟값 출력 



ININPUT = input()
Zbinarystrings = list(ININPUT.split('1'))
Fbinarystrings = list(ININPUT.split('0'))

save = []
save.append(len(Zbinarystrings)-Zbinarystrings.count(''))
save.append(len(Fbinarystrings)-Fbinarystrings.count(''))

print(min(save))

