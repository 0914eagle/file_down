
def min_packages(t, test_cases):
    results = []
    for i in range(t):
        n, k = test_cases[i]
        if n <= k:
            results.append(1)
        else:
            min_packages = n
            for j in range(1, int(n**0.5) + 1):
                if n % j == 0:
                    if j <= k:
                        min_packages = min(min_packages, n // j)
                    if n // j <= k:
                        min_packages = min(min_packages, j)
            results.append(min_packages)
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    test_cases.append((n, k))

# Output
results = min_packages(t, test_cases)
for res in results:
    print(res)
