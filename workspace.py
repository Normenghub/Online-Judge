
friend = {'v' : 'q' ,'q' : 'q'}
def whoParent(a):
    if friend[a] == a:

        return a 
    else:
        return whoParent(friend[a])
    

print(whoParent('v'))