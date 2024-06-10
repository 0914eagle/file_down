
n = int(input())
a = list(map(int, input().split()))

s = sum(a[:n])
t = sum(a[n:])
if s == t:
    print(-1)
else:
    print(*a)

