
import sys
n = int(sys.stdin.readline().strip())
a = [int(sys.stdin.readline().strip()) for _ in range(n)]

sa = [a[0]]
sb = [0]
for i in range(1, n):
    sa.append(a[i]+sa[i-1])
    sb.append(-a[i]+sb[i-1])

if sa[-1] > sb[-1]:
    print('first')
elif sa[-1] < sb[-1]:
    print('second')
elif sa > sb:
    print('first')
elif sa < sb:
    print('second')
else:
    print('second')
