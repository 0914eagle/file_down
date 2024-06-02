
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    test_days = [0] * max_duration

    for d in durations:
        for i in range(d):
            test_days[i] = max(test_days[i], i + 1)

    return sum(test_days)

# Read input
k = int(input())
durations = [int(input()) for _ in range(k)]

# Calculate and print the shortest test scheme
print(shortest_test_scheme(k, durations))
