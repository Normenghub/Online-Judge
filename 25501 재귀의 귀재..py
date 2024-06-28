def recursion(s, l, r):
    if l >= r: return f'1,{r}'
    elif s[l] != s[r]: return f'0,{r}'
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

count = 0
for i in range(int(input())):
    s = input()
    print(f"{isPalindrome(s)[0]} {len(s) - int(isPalindrome(s)[2:])}")