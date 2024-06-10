
nm = input().split()
n = int(nm[0])
m = int(nm[1])

if n > m:
    n, m = m, n

if n == 1:
    print(min(m, 3))
elif n == 2:
    print(min(m, 3) * 2)
else:
    print(min(m, 4) + (m - min(m, 4)) // 2 * 2)

