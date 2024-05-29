
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    count = [durations.count(d) for d in range(1, max_duration + 1)]
    return max_duration + sum([d * count[d - 1] for d in range(1, max_duration)]) 

# Input processing
k = int(input())
durations = [int(input()) for _ in range(k)]

# Call the function and print the output
print(shortest_test_scheme(k, durations))
