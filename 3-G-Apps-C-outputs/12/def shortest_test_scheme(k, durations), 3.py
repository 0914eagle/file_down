
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    test_days = max_duration - 1  # Initial test days based on the longest allergen duration

    for day in range(1, max_duration):
        active_allergens = [d for d in durations if day <= d]
        if len(active_allergens) > 1:
            test_days += 1

    return test_days + 1  # Add one more day for the final examination

# Input processing
k = int(input())
durations = []
for _ in range(k):
    durations.append(int(input()))

# Call the function and print the output
print(shortest_test_scheme(k, durations))
