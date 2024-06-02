
def min_packages(n, k):
    min_packages = n
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i <= k:
                min_packages = min(min_packages, n // i)
            if n // i <= k:
                min_packages = min(min_packages, i)
    return min_packages

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(min_packages(n, k))
