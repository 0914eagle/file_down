
def find_time_limit(n, m, correct_times, wrong_times):
    correct_times.sort()
    wrong_times.sort()
    
    min_v = correct_times[0] * 2
    
    if min_v >= wrong_times[0]:
        return -1
    
    return min_v

# Input
n, m = map(int, input().split())
correct_times = list(map(int, input().split()))
wrong_times = list(map(int, input().split()))

# Output
result = find_time_limit(n, m, correct_times, wrong_times)
print(result)
