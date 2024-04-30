'''
maps = []
howManyApples = []
for i in range(5):
    smallMaps = list(map(int,input().split()))
    maps.append(smallMaps)
r,c =map(int,input().split())
sum = 0
if r == 0 and c == 0:
#두개
        if maps[r][c+1] == 1:
            sum +=1
        if maps[r+1][c] == 1:
            sum +=1    

elif r == 0 and c == 4:
#두 개
        if maps[r][c-1] == 1:
            sum +=1
        if maps[r+1][c] == 1:
            sum +=1    
elif r == 4 and c ==0 :
        if maps[r][c+1] == 1:
            sum +=1
        if maps[r-1][c] == 1:
            sum +=1 
elif r == 4 and c == 4:
        if maps[r][c-1] == 1:
            sum +=1
        if maps[r-1][c] == 1:
            sum +=1 

elif r == 0 and c != 4 or 0:
        if maps[r+1][c] == 1:
            sum +=1
        if maps[r][c-1] == 1:
            sum +=1 
        if maps[r][c+1] == 1:
            sum +=1             
elif r == 4 and c != 4 or 0:
        if maps[r-1][c] == 1:
            sum +=1
        if maps[r][c-1] == 1:
            sum +=1 
        if maps[r][c+1] == 1:
            sum +=1     
elif c == 0 and r != 0 or 4:
        if maps[r][c+1] == 1:
            sum +=1
        if maps[r-1][c] == 1:
            sum +=1 
        if maps[r+1][c] == 1:
            sum +=1     
elif c ==4 and r != 0 or 4:
        if maps[r][c-1] == 1:
            sum +=1
        if maps[r-1][c] == 1:
            sum +=1 
        if maps[r+1][c] == 1:
            sum +=1     
else:
        if maps[r][c+1] == 1:
            sum +=1
        if maps[r][c-1] == 1:
            sum +=1 
        if maps[r+1][c] == 1:
            sum +=1  
        if maps[r-1][c] == 1:
            sum +=1              

print(sum)            

#노가다 

'''

maps = []
for i in range(5):
    smallMaps = list(map(int,input().split()))
    maps.append(smallMaps)
길미분 = list(map(int,input().split()))
def findDirection(maps,길미분):
    dd =[[-1,0],[1,0],[0,-1],[0,1]]

    for dr, dc in dd:
        r,c = 길미분[0]+ dr, 길미분[1] + dc
        if 나가지마(r,c) and maps[r][c] == 1:
            return 1
 
    return 0



def 나가지마(r,c):
    return 0<=r<=4 and 0<= c<= 4

print(findDirection(maps,길미분))

