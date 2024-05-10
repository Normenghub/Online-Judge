n = int(input())

lists = list(map(int,input().split()))
lists.sort()
if len(lists) ==1:
    print(lists[0]*lists[0])
else:
    print(lists[0]*lists[-1])    