n,m = map(int,input().split())
dic = {}
lists = []
for i in range(m):
    a ,b = map(int,input().split())
    dic[a]=i+1
    dic[b]=i+1

lists = sorted(dic.items(), key = lambda x : x[0])

if n < len(lists):
   print(lists[n-1][1])
else:
   x = n % len(lists)
   print(lists[x-1][1])   