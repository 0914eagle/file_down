
for i in range(1, n):
    a[i] = min(a[i], len(a[i - 1]))

for i in range(n - 1, 0, -1):
    a[i] = min(a[i], len(a[i + 1]))

for i in range(n):
    a[i] -= a[i + 1]

print('a', a)

a[0] -= a[1]
for i in range(1, n):
    a[i] -= a[i - 1]

print('a', a)

s = []

for i in range(n + 1):
    s.append('a' * a[i])

for i in range(n):
    s[i] += chr(ord('b') + i) * (len(s[i + 1]) - len(s[i]))

print('s', s)

for i in range(n + 1):
    print(s[i])
