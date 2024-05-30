import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(int,input().split()))
arr.sort()
s=[]
for v in range(1,len(arr)):
        s.append(arr[v]-arr[v-1])
s.sort(reverse=True)
print(sum(s[k-1:]))
'''
3 6 7 8 10 12 14 15 18 20
 3 1 1 2  2  2  1  3  2
1 3 6 7 9
 2 3 1 2 

'''