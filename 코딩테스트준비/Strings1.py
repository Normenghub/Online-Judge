strings = input()

num = int(input())

if len(strings) < num:
 x = strings[len(strings)-1] * (num-len(strings))
 strings += x
 print(strings)   
elif len(strings) == num:
    print(strings)