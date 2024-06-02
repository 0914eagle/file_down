
s = input()
if s[0] == 'a' and s[1] == 'b' and s[2] == 'c':
    print('Yes')
elif s[0] == 'a' and s[1] == 'c' and s[2] == 'b':
    print('Yes')
elif s[0] == 'b' and s[1] == 'a' and s[2] == 'c':
    print('Yes')
elif s[0] == 'b' and s[1] == 'c' and s[2] == 'a':
    print('Yes')
elif s[0] == 'c' and s[1] == 'a' and s[2] == 'b':
    print('Yes')
elif s[0] == 'c' and s[1] == 'b' and s[2] == 'a':
    print('Yes')
else:
    print('No')

