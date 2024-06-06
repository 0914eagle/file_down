
n = int(input())
s = input()

if s.count('?') % 2 == 1:
    print('Monocarp')
else:
    if s.count('?') == 0:
        if int(s[:n//2]) == int(s[n//2:]):
            print('Bicarp')
        else:
            print('Monocarp')
    else:
        print('Bicarp')
