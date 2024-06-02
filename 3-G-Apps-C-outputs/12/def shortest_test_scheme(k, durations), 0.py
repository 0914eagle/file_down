
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    scheme_days = max_duration
    for d in durations:
        scheme_days += d - 1
    return scheme_days

# Input processing
k = int(input())
durations = []
for _ in range(k):
    durations.append(int(input()))

# Calculate and output the shortest test scheme
print(shortest_test_scheme(k, durations))
