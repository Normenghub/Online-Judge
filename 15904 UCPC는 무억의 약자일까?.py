import sys

strings = sys.stdin.readline().rstrip()
arr = ['U','C','P','C']
for i in strings:
    if len(arr) == 0:
        break
    if i == arr[0]:
        del arr[0]
        continue
    if len(arr) == 0:
        break
if len(arr) == 0:
    print("I love UCPC")
else:
    print("I hate UCPC")        
