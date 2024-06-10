
n, a, b, c, d = map(int, input().split())
print(n**2 - max(n-a, 0) * max(n-b, 0) - max(n-c, 0) * max(n-d, 0))

