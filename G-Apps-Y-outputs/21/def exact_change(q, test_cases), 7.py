
def exact_change(q, test_cases):
    results = []
    for i in range(q):
        a, b, n, S = test_cases[i]
        max_x = min(a, S // n)
        if max_x * n + b >= S:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input parsing
q = int(input())
test_cases = []
for _ in range(q):
    a, b, n, S = map(int, input().split())
    test_cases.append((a, b, n, S))

# Solve and output results
results = exact_change(q, test_cases)
for result in results:
    print(result)
