
#codeforces
import sys
#sys.stdin = open('in.txt', 'r')
#sys.stdout = open('out.txt', 'w')

n, m = map(int, input().split())
x = []
y = []
for i in range(n):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

flag = True
for i in range(m):
    _x, _y = map(int, input().split())
    if flag:
        if (_x - x[0])**2 + (_y - y[0])**2 == (x[0] - x[1])**2 + (y[0] - y[1])**2:
            continue
        else:
            flag = False
    else:
        if (_x - x[0])**2 + (_y - y[0])**2 == (x[0] - x[1])**2 + (y[0] - y[1])**2:
            flag = True

if flag:
    print('YES')
else:
    print('NO')

