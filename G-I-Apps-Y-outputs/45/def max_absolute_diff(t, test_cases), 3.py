
def max_absolute_diff(t, test_cases):
    results = []
    for n, m in test_cases:
        if n == 1:
            results.append(0)
        elif n == 2:
            results.append(min(m, 2))
        else:
            if m >= 2 * n:
                results.append(m)
            else:
                remaining = m - n
                first_half = n // 2
                second_half = n - first_half
                result = first_half * (n - first_half) + second_half * (n - second_half)
                results.append(result)
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

# Output
results = max_absolute_diff(t, test_cases)
for res in results:
    print(res)
