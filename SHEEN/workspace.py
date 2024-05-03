import copy
a = [1,2,3,4]

b= copy.deepcopy(a)

a.append(4)
print(a)
print(b)