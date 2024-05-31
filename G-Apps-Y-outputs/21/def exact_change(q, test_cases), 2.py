
def exact_change(q, test_cases):
    results = []
    for i in range(q):
        a, b, n, S = test_cases[i]
        remaining = S - min(S // n, a) * n
        if remaining <= b:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input
q = 4
test_cases = [
    [1, 2, 3, 4],
    [1, 2, 3, 6],
    [5, 2, 6, 27],
    [3, 3, 5, 18]
]

# Output
results = exact_change(q, test_cases)
for result in results:
    print(result)
