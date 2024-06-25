n = 1
def selfNumber(n):
    nstr = str(n)
    for i in nstr:
        n += int(i)
    return n    
arr = []
for i in range(1,10000):
    arr.append(selfNumber(i))
arr = list(set(arr))
s = [i for i in range(1,10000)]
for i in range(29):
    del arr[-1]
for k in arr:
    s.remove(k)
for z in s:
    print(z)