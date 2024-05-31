
def find_most_suitable_tl(n, m, correct_times, wrong_times):
    correct_times.sort()
    wrong_times.sort()
    
    v = correct_times[-1] # Set initial TL to be the maximum correct running time
    
    if v >= wrong_times[0]: # Check if any wrong solution passes the system testing
        return -1
    
    for a in correct_times:
        if 2*a <= v: # Check if all correct solutions pass the system testing
            return v
    
    return -1

n, m = map(int, input().split())
correct_times = list(map(int, input().split()))
wrong_times = list(map(int, input().split()))

result = find_most_suitable_tl(n, m, correct_times, wrong_times)
print(result)
