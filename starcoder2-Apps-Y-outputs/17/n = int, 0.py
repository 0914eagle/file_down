
n = int(input())
a = list(map(int, input().split()))

a.sort()

y = 0
z = 0

for i in range(n):
    if a[i] == 0:
        continue
    if a[i] == a[i - 1]:
        y += 1
    else:
        y += 1
        z = a[i]

print(y, z)

