maps = []
count = 0
def outLines(drr,dcc):
    return 0<= drr<= 7 and 0 <= dcc<=7
for w in range(8):
    for ww in range(8):
        maps.append([w,ww])
dic = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
dd = [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
위치 = input()
위치 = list(위치)
r = dic[위치[0]]
c = int(위치[1])-1
for dr,dc in dd:
    drr = r+ dr
    dcc = c + dc
    
    if outLines(drr,dcc):
        count+=1
    else:
        continue
print(count)        

