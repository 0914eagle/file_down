
def min_mistakes(n, s, reports):
    mistakes = 0
    reported_superiors = [0] * n

    for i in range(n):
        if i + 1 != s:
            reported_superiors[reports[i]] += 1

    for i in range(n):
        if i + 1 != s and reported_superiors[i] != reports[i]:
            mistakes += 1

    return mistakes

# Read input
n, s = map(int, input().split())
reports = list(map(int, input().split()))

# Print output
print(min_mistakes(n, s, reports))
```
