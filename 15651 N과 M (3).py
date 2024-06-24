import itertools
import sys 
a,b = map(int,sys.stdin.readline().split())
arr = [x for x in range(1,a+1)]    

for k in itertools.product(arr, repeat=b):
    for z in range(len(k)):
        print(k[z],end=" ")
    print()    
