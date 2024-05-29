
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    schedule = [0] * (max_duration + 1)
    
    for d in durations:
        for i in range(1, d + 1):
            schedule[i] += 1
    
    return max(schedule)

# Read input
k = int(input())
durations = [int(input()) for _ in range(k)]

# Call the function and print the result
print(shortest_test_scheme(k, durations))
