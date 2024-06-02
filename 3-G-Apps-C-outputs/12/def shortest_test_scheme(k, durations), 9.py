
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    return max_duration + k - 1

# Read input
k = int(input())
durations = []
for _ in range(k):
    durations.append(int(input()))

# Calculate and print the shortest test scheme
print(shortest_test_scheme(k, durations))
