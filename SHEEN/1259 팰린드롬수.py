while True:
    strings = input()
    if strings == '0':
        break
    elif strings == strings[::-1]:
        print('yes')

    else:
        print('no')    