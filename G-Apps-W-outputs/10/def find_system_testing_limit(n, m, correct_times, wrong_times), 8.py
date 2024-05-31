
def find_system_testing_limit(n, m, correct_times, wrong_times):
    min_tl = max(max(correct_times), 2 * min(correct_times))
    
    if min_tl >= min(wrong_times):
        return -1
    return min_tl

# Read input
n, m = map(int, input().split())
correct_times = list(map(int, input().split()))
wrong_times = list(map(int, input().split()))

# Call the function and print the result
result = find_system_testing_limit(n, m, correct_times, wrong_times)
print(result)
