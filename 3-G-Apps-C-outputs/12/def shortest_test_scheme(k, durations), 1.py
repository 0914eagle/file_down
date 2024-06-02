
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    scheme_duration = 2 * max_duration - 1
    return scheme_duration

# Read input
k = int(input())
durations = []
for _ in range(k):
    durations.append(int(input()))

# Calculate and print the shortest test scheme duration
print(shortest_test_scheme(k, durations))
