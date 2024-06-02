
n = int(input())
a = list(map(int, input().split()))

a.sort()

x = a[0]
z = a[1] - a[0]
y = (a[-1] - a[0]) // z

print(y, z)

