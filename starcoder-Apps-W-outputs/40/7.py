
# python 3.6
a = int(input())
s = list(input())
c = s.count('C')
m = s.count('M')
y = s.count('Y')
if c == 0 and m == 0 and y == 0:
    print('Yes')
elif c >= 2 and m >= 2 and y >= 2:
    print('Yes')
elif c >= 1 and m >= 1 and y >= 1:
    if c == 1 and m == 1 and y == 1:
        print('Yes')
    else:
        print('No')
else:
    print('No')
