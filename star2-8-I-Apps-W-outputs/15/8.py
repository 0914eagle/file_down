
n = int(input())
a = list(map(int, input().split()))

b = sorted(a)
s = sum(b[:n])
t = sum(b[n:])
if s == t:
    print(-1)
else:
    print(' '.join(map(str, b)))

