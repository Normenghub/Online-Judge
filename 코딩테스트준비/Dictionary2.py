strings = list(input().split())
nomordic  = {}


for i in range(len(strings)):
    try:
        nomordic[strings[i]] = strings.count(strings[i])
    except:
        continue

nomordiclist = list(nomordic.items())
nomordiclist.sort(key = lambda x: x[0])
for name, value in nomordiclist:
    print(f"{name} {value}")



