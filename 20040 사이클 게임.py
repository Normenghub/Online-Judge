import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

n , k = map(int,input().split())
count = 0
arr = []

def findParents(v):
    if arr[v] == v:
        return v
    else:
        arr[v] = findParents(arr[v])
        return findParents(arr[v])

def union(a,b):
    global count
    one = findParents(a)
    two = findParents(b)
    if one == two:
        print(count+1)
        exit()
    if one > two:
        arr[two] = one
    else:
        arr[one] = two

for i in range(n): arr.append(i)

for _ in range(k):
    a,b = map(int,input().split())

    union(a,b)
    count +=1
 
print(0)