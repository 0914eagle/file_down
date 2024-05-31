
def find_time_limit(n, m, correct_times, wrong_times):
    max_correct_time = max(correct_times)
    min_correct_time = min(correct_times)
    min_wrong_time = min(wrong_times)
    
    for v in range(max(min_wrong_time, 2*min_correct_time), min_correct_time*2+1):
        if all(time <= v for time in correct_times) and any(time <= v/2 for time in correct_times) and all(time > v for time in wrong_times):
            return v
    return -1

n, m = map(int, input().split())
correct_times = list(map(int, input().split()))
wrong_times = list(map(int, input().split()))

result = find_time_limit(n, m, correct_times, wrong_times)
print(result)
