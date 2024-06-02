
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    test_days = max_duration  # Start with the maximum duration
    
    for day in range(1, max_duration + 1):
        active_allergens = [d for d in durations if day % d == 0]  # Find active allergens on the current day
        if len(active_allergens) > 1:  # If there are multiple active allergens, extend the test
            test_days += 1
    
    return test_days

# Read input
k = int(input())
durations = [int(input()) for _ in range(k)]

# Calculate and print the shortest test scheme
print(shortest_test_scheme(k, durations))
