import sys
input =sys.stdin.readline
n,m,k = map(int,input().split())
arr = []
for _ in range(n):
    f = int(input())
    arr.append(f)
tree = [0] * (len(arr) * 4)


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

# 재귀로 트리구조 만듬

# 구간의 합은 '범위 안에 있는 경우'

def interval_sum(start, end, index, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return tree[index]
    # 그렇지 않다면 두 부분으로 나누어 합을 구하기
    mid = (start + end) // 2
    # start와 end가 변하면서 구간 합인 부분을 더해준다고 생각하면 된다.
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, what, value):
    # 범위 밖에 있는 경우
    if what < start or what > end:
        return
    # 범위 안에 있으면 내려가면서 다른 원소도 갱신
    tree[index] += (value-arr[what-1])
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)

init(0,n-1,1)
print(tree)
for _ in range(k+m):
    a , b ,c = map(int,input().split())
    if a == 1:
        update(0,len(arr)-1,1,b,c)
        print(tree)
    else:
       print( interval_sum(0,len(arr)-1,1,b,c))
