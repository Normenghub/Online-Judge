strings = list(input().split())
nomordic  = {}


for i in range(len(strings)):
    try:
        nomordic[strings[i]] = strings.count(strings[i])
    except:
        continue

strings = list(set(strings))
for k in strings:
    print(f"{k} {nomordic[k]}")



