import sys
input = sys.stdin.readline
arr = []
for i in range(3):
    x= input().rstrip()
    try:
        arr.append((int(x),0))
    except:
        arr.append((x,1))    
for k in range(3):
    if arr[k][1]  ==0:
        index = k
        x = arr[k][0]
        if index == 0:
            c = x+3
        elif index == 1:
            c = x + 2
        elif index == 2:
            c = x + 1
        break
    else:
        continue
if c % 3 == 0 and c % 5 == 0:
    print('FizzBuzz')
elif c % 3 != 0 and c % 5 == 0:
     print('Buzz')
elif c % 3 == 0 and c % 5 != 0:
     print('Fizz')
else:
    print(c)
