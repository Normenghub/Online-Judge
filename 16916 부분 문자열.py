strings = input()
partStrings = input()


def solution(strings,partStrings):

 if partStrings in strings:
     return 1
 else:
     return 0
print(solution(strings,partStrings))       