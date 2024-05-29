
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    days = max_duration
    total_duration = sum(durations)
    while days * k - (k-1) < total_duration:  # Adjust the end condition considering inactive periods
        days += max_duration
    return days

k = int(input())
durations = [int(input()) for _ in range(k)]
result = shortest_test_scheme(k, durations)
print(result)
```
