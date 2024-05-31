
def find_time_limit(n, m, correct_times, wrong_times):
    v = max(max(correct_times), 2 * min(correct_times))
    if v >= min(wrong_times):
        return -1
    return v

# Input
n, m = map(int, input().split())
correct_times = list(map(int, input().split()))
wrong_times = list(map(int, input().split()))

# Output
result = find_time_limit(n, m, correct_times, wrong_times)
print(result)
