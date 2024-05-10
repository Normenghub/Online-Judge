dic = {"ChongChong" : 1 }
sum = 0
n = int(input())
for i in range(n):
    a = list(input().split())
    person1 = a[0]
    person2 = a[1]
    if person1 not in dic and person2 not in dic:
        continue
    else:
        dic[person1] =1
        dic[person2] =1
print(len(dic))        