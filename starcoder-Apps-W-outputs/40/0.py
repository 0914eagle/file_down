
n = int(input())
s = input()

if s.count('?') > 2:
    print('Yes')
elif s.count('?') == 2:
    if 'C' in s and 'M' in s and 'Y' in s:
        print('Yes')
    else:
        print('No')
else:
    print('No')
