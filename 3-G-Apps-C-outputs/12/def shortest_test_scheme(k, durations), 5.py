
def shortest_test_scheme(k, durations):
    max_duration = max(durations)
    test_days = max_duration
    for i in range(1, max_duration + 1):
        count = sum(1 for d in durations if i <= d)
        if count > 1:
            test_days += 1
    return test_days

# Input reading
k = int(input())
durations = []
for _ in range(k):
    durations.append(int(input()))

# Call the function and print the result
result = shortest_test_scheme(k, durations)
print(result)
