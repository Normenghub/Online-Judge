N, K = map(int,input().split())

arr = []
savearr = []
#  1 4 
#  3 6 2 7 5 1 4
#  2 4 1 3 2 0 0
index = K-1
for i in range(1, N+1):
    arr.append(i)

while len(savearr) < N:
    if index < len(arr)-1:
        savearr.append(arr[index])
        del arr[index]
        index +=2
    elif index == len(arr)-1:
        index %= 3
        savearr.append(arr[index])
        del arr[index]
        index +=2
    else:
        







print(arr)
print(savearr)