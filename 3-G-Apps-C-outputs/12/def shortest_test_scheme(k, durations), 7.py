
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    test_days = max_duration
    for i in range(1, max_duration):
        count = sum(1 for d in durations if i % d == 0)
        if count >= 2:
            test_days += 1
    return test_days

# Read input
k = int(input())
durations = [int(input()) for _ in range(k)]

# Calculate and print the shortest test scheme
print(shortest_test_scheme(k, durations))
