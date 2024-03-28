import sys

input = sys.stdin.readline

num = int(input())

list1 = list(map(int, input().split()))

list2 = list(set(list1))

list2.sort()

list3 = [i for i in range(len(list2))]

nomoredic = {key:value for key, value in zip(list2, list3)}


for num in list1:
    print(nomoredic[num],end=" ")
