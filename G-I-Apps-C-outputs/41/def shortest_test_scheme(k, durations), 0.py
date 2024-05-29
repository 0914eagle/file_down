
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    scheme_days = max_duration
    for i in range(1, max_duration + 1):
        active_allergens = [d for d in durations if i <= d]
        if len(active_allergens) > 1:
            scheme_days += 1
    return scheme_days

# Read input
k = int(input())
durations = []
for _ in range(k):
    durations.append(int(input()))

# Call the function and print the output
print(shortest_test_scheme(k, durations))
```
