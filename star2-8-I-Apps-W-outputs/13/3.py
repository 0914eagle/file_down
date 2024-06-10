
import sys
n, t = map(int, input().split())
a = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    if a[0] > a[1]:
        print('Bigger')
    elif a[0] == a[1]:
        print('Equal')
    else:
        print('Smaller')
elif t == 3:
    a = sorted(a[:3])
    print(a[1])
elif t == 4:
    print(sum(a))
elif t == 5:
    print(sum(i for i in a if i % 2 == 0))
elif t == 6:
    s = ''
    for i in a:
        s += chr(ord('a') + i % 26)
    print(s)
else:
    i = 0
    while 0 <= i < n:
        if i == n - 1:
            print('Done')
            break
        i = a[i]
    else:
        print('Cyclic')

