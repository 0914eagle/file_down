
n, t, c = map(int, input().split())
a = list(map(int, input().split()))

l, r = -1, -1

if n == 1:
    print(0)
    exit()

if t == 0:
    print(c)
    exit()

s = 0

for i in range(n):
    if a[i] <= t and r < i:
        l, r = i, i
        while r < n and a[r] <= t:
            r += 1
        s += r - l - c + 1
    else:
        r += 1

print(s)
