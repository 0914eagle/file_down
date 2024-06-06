
n = int(input())
s = input()

if n == 2:
    print('Bicarp')
else:
    if s.count('?') % 2 == 0:
        print('Bicarp')
    else:
        print('Monocarp')
