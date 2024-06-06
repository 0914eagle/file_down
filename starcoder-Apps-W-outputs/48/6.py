
a, b = input(), list(map(int, input().split()))
s = ''
for i in range(1, 10):
    t = min(a // b[i - 1], 9 - i)
    a -= t * b[i - 1]
    s += str(t + i) * t
if a == 0 and s[0] != '0':
    print(s)
else:
    print(-1)
