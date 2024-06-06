
n = int(input())
s = input()

if s.count('?') % 2 == 1:
    print('Monocarp')
else:
    if s.count('?') == 0:
        print('Bicarp')
    else:
        if s.count('?') % 4 == 0:
            print('Bicarp')
        else:
            print('Monocarp')
