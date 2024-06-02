
n = int(input())
a = list(map(int, input().split()))

a.sort()

x = a[-1]
y = 0
z = 0

for i in range(n - 1, -1, -1):
    if a[i] == x:
        y += 1
    else:
        z = x - a[i]
        break

print(y, z)

