
n, k = [int(x) for x in input().split()]
if n <= k:
    print(n - 1)
else:
    print(k ^ (k - 1))

