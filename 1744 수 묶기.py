import sys
input = sys.stdin.readline
n = int(input())
arr = []
miarr =[]
zero = []
result = 0
one = []
for i in range(n):
    x= int(input())
    if x > 1:
        arr.append(x)
    elif x <0:
        miarr.append(x)
    elif x ==1:
        one.append(x)    
    else:
        zero.append(x)        
arr.sort(reverse=True)
miarr.sort()
def arrsum(arr):
  arrsums = 0
  if len(arr) >2:
    if len(arr) % 2 == 0:
        for arrr in range(0,len(arr),2):
          arrsums+= (arr[arrr] * arr[arrr+1])
        return arrsums
    else:    
        for arrr in range(1,len(arr),2):
          arrsums+= (arr[arrr] * arr[arrr-1]) 
        arrsums += arr[-1]
        return arrsums  
  elif len(arr)==2:
      if arr[0] == 1:
          arrsums += sum(arr)
      else:
          arrsums += (arr[1] * arr[0])    
      return arrsums    
  elif len(arr) ==1:
      arrsums += arr[0]
      return arrsums
  else:
     return 0    


def miarrsum(miarr,zero):
  arrsumss = 0
  if len(miarr) >=2:
    if len(miarr) % 2 == 0:
        for miarrr in range(0,len(miarr),2):
          arrsumss+= (miarr[miarrr] * miarr[miarrr+1])
        return arrsumss   
    else:    
        for miarrr in range(1,len(miarr),2):
          arrsumss+= (miarr[miarrr] * miarr[miarrr-1])    
        if len(zero) > 0:
               pass
        else:
           arrsumss += miarr[-1]   
        return arrsumss           
  elif len(miarr) == 1:
        if len(zero) > 0:
               pass
        else:
           arrsumss += miarr[0]  
        return arrsumss         
  else:
     return arrsumss       
result = arrsum(arr) + miarrsum(miarr,zero)
if len(one)>0:
    result += sum(one)
else:
    pass    

print(result)


