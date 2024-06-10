
n, k = map(int, input().split())
if n == k:
    print(n)
else:
    print(n ^ (n-1))

