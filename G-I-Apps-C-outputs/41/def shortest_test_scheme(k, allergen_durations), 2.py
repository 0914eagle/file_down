
def shortest_test_scheme(k, allergen_durations):
    max_duration = max(allergen_durations)
    total_days = max_duration  # Start with the maximum duration
    for day in range(1, max_duration):
        active_allergens = [d for d in allergen_durations if day % d != 0]
        if not active_allergens:  # No active allergens
            total_days = day
            break
    return total_days

# Reading input
k = int(input())
allergen_durations = [int(input()) for _ in range(k)]

# Call the function and print output
output = shortest_test_scheme(k, allergen_durations)
print(output)
```
