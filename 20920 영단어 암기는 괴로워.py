import sys
n,k = map(int,sys.stdin.readline().split())
arr = []
dic = {}
subDic = {}
for _ in range(n):
   strings = sys.stdin.readline().rstrip()
   if len(strings) >= k:
      if strings not in dic:
         dic[strings] = 1
      else:
         dic[strings]+=1
   else:
      continue
keys1 = list(dic.keys())
for m in keys1:
   if dic[m] not in subDic:
      subDic[dic[m]] = [m]
   else:
      subDic[dic[m]].append(m)   
keys2=  list(subDic.keys())
keys2.sort(reverse=True)
for w in keys2:
   subDic[w].sort(key=lambda x: (-len(x),x))
for xx in keys2:
  for x in subDic[xx]:
     print(x)  