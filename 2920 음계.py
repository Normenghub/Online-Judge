import sys 
input = sys.stdin.readline
dic ={1:'c',2:'d',3:'e',4:'f',5:'g',6:'a',7:'b',8:'C'}
lists = list(map(int,input().split()))
result =''
for i in lists:
    result += dic[i]
if result == 'cdefgabC':
    print('ascending')
elif result == 'Cbagfedc':
    print('descending')
else:
    print('mixed')            