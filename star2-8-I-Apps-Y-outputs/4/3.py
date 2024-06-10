
n = int(input())
a = list(map(int, input().split()))
a.sort()
s = 0
t = 0
for i in range(n):
    if i < n // 2:
        s += a[i]
    else:
        t += a[i]
print(abs(s - t))

