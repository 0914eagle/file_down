
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    total_days = max_duration
    for i in range(1, max_duration):
        count = sum(1 for d in durations if i <= d)
        if count >= 2:
            total_days += 1
    return total_days

# Read input
k = int(input())
durations = [int(input()) for _ in range(k)]

# Call the function and print the result
print(shortest_test_scheme(k, durations))
