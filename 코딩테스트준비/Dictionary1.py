nomordic = {}
sum =0
a , b = map(int,input().split())


for i in range(a):
    num1,num2 = map(str,input().split())
    nomordic[num1] = num2

sumlist = list(input().split())

for k in range(b):
    sum += int(nomordic[sumlist[k]])

print(sum)
