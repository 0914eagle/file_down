

n = int(input())
l = [int(i) for i in input().split()]
d = [0] * (n+2)
for i in range(1, n+1):
    d[i] = max(d[i-1], d[i-2] + l[i-1])
for i in range(n, 0, -1):
    d[i] = max(d[i], d[i+1], d[i+2] + l[i-1])
print(d[n])

