
def max_visitors(t, cases):
    result = []
    for case in cases:
        a, b, c = case
        max_visitors = min(a, b, c) + (a + b + c - min(a, b, c)) // 2
        result.append(max_visitors)
    return result

# Input
t = int(input())
cases = []
for _ in range(t):
    a, b, c = map(int, input().split())
    cases.append((a, b, c))

# Output
result = max_visitors(t, cases)
for res in result:
    print(res)
```
