N, K = map(int,input().split())

arr = []
savearr = []
#  1 2 3 4 5 6 7
#  3 6 2 5 1 4
index = K-1
for i in range(1, N+1):
    arr.append(i)

while len(savearr) < N:
    if index <= len(arr):
        savearr.append(arr[index])
        index +=3
    else:
        index -= N
        savearr.append(arr[index])
        index +=3





print(arr)
print(savearr)