def solution(strings):
    T = ''
    i = 0
    while i<len(strings):
        if strings[i] != 'a' and strings[i] !=  'A':
            T += strings[i]
            i +=1
            continue

        j = i +1
        while j<len(strings):
            if strings[j]!= 'a' and strings[j] != 'A':
                break
            j +=1
        if j-1 ==1:
           T +=strings[i]    
        else:
            T+=strings[i].lower()

        i = j


    return T           
strings = input()
print(solution(strings))