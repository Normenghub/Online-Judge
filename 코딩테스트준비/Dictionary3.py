n = input()
m = list(set(list(input().split())))
nomordic = {}
for i in n.split():
   nomordic[i] = 1

for j in m:
   del nomordic[j]

nomordic2 = sorted(nomordic)





for k in nomordic2:
   print(k)
