
def max_visitors(t, test_cases):
    for case in test_cases:
        a, b, c = case
        max_visitors = min(a, b, c) + max(min(a, b), min(b, c), min(a, c)) + min(max(a, b), max(b, c), max(a, c))
        print(max_visitors)

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    a, b, c = map(int, input().split())
    test_cases.append((a, b, c))

# Call function with input
max_visitors(t, test_cases)
```
