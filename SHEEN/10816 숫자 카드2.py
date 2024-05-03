import sys
input = sys.stdin.readline
nomordic = {}

num1 = int(input())

numbers =list(map(int,input().split()))

for i in numbers:
    if i in nomordic:
        nomordic[i] +=1
    else:
        nomordic[i] =1

num2 = int(input())

numbers2 =list(map(int,input().split()))

for k in numbers2:
    if k in nomordic:
        print(f"{nomordic[k]}",end = " ")
    else:
        print("0", end = " ")    