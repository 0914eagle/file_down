
def min_packages(t, test_cases):
    results = []
    for n, k in test_cases:
        if n <= k:
            results.append(1)
        else:
            min_packages = float('inf')
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    if i <= k:
                        min_packages = min(min_packages, n // i)
                    if n // i <= k:
                        min_packages = min(min_packages, i)
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