
n = int(input())
a = list(map(int, input().split()))

a.sort()

y = 0
z = 0

for i in range(n):
    if a[i] > 0:
        y += a[i]
        z = a[i]
        break

print(y, z)

