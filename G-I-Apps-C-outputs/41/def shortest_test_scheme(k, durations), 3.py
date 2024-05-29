
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    count = [0] * (max_duration + 1)
    for d in durations:
        count[d] += 1
    
    total_days = max_duration
    for i in range(1, max_duration):
        if sum(count[i:]) <= i:
            total_days = max(total_days, i + max_duration)
    
    return total_days

# Input parsing
k = int(input())
durations = []
for _ in range(k):
    durations.append(int(input()))

print(shortest_test_scheme(k, durations))
```
