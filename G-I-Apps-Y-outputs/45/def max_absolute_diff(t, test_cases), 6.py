
def max_absolute_diff(t, test_cases):
    results = []
    for i in range(t):
        n, m = test_cases[i]
        if n == 1:
            results.append(0)
        elif n == 2:
            results.append(2)
        else:
            if n % 2 == 0:
                results.append(m * 2)
            else:
                results.append(m * 2 - 2)
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

# Get results
results = max_absolute_diff(t, test_cases)

# Print results
for res in results:
    print(res)
```
