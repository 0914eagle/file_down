
def coffee_like(s):
    return s[2] == s[3] and s[4] == s[5]

s = input()
if coffee_like(s):
    print('Yes')
else:
    print('No')

