
n = int(input())
a = list(map(int, input().split()))
a.sort()

y = 0
z = 0

for i in range(n):
    if a[i] == a[0]:
        y += 1
    else:
        z = a[i] - a[0]
        break

print(y, z)

