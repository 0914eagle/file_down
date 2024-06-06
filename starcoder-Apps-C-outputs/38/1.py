
n, k = map(int, input().split())
print((pow(2, n, 1000000007) - 1) * (pow(n, k, 1000000007) + 1) % 1000000007)
