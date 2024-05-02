
'''
def solution(num,first,last,count):
 for i in range(int(first),int(last)+1):
     if "0" in str(i):
          continue
  
     if num ==1:
         return 9
     elif num >1:
      for k in range(len(str(i))-1):
          if abs(int(str(i)[k]) - int(str(i)[k+1])) > 2:
               break
          else:
               count +=1  
               continue
       
          

     
 return count       
''' #<<<<<<<<<<<<<<< 너무 느림 완전탐색

def ik(A):

 p = A %10
 A //=10
 if p == 0:
    return False
 while A>0:
    c = A %10
    A //=10

    if c == 0 or abs(p-c) >2:
       return False
    
    p = c
 return True   


def solution(num):
    count =0

    for i in range(10**(num-1),10**num):
        if ik(i):
            count +=1
    return count            

num = int(input())
print(solution(num))

#  1 2 3 4 5 6 7 8 9
#  11 12 13 
#  111 112 113 121 122 123 131 132 133 141 142 143 