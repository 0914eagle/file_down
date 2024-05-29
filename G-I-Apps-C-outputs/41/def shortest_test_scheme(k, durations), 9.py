
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    scheme_duration = max_duration
    for i in range(1, max_duration + 1):
        if all(i % d == 0 for d in durations):
            scheme_duration = i
            break
    return scheme_duration

# Read input
k = int(input())
durations = [int(input()) for _ in range(k)]

# Calculate and print output
print(shortest_test_scheme(k, durations))
```
