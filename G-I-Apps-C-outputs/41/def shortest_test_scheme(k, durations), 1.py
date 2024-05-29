
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    return max_duration + (k - 1)

# Read input
k = int(input())
durations = [int(input()) for _ in range(k)]

# Output the result
print(shortest_test_scheme(k, durations))
