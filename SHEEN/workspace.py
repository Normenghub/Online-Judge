boysandgirls = list(input().split())

hour = 0

min = 0

for i in range(len(boysandgirls)):
    hour += int(boysandgirls[i][0]+boysandgirls[i][1])
    min += int(boysandgirls[i][3]+boysandgirls[i][4])


if min >=60:
    hour += min/60
    min =0
    min +=min % 60    
if hour < 10 and min < 10:
  print(f"0{int(hour)}:0{int(min)}")
elif hour<10 and min>=10:  
  print(f"0{int(hour)}:{int(min)}")
elif min<10 and hour>=10:
     print(f"{int(hour)}:0{int(min)}") 
else:
     print(f"{int(hour)}:{int(min)}")      

