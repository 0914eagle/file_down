
def max_bowls(n, T, times):
    times.sort()
    
    total_eaten = 0
    time_passed = 0
    for time in times:
        if time > T:
            break
        if time >= time_passed + 1:
            total_eaten += 1
            time_passed = time
        else:
            if time + 1 <= T:
                total_eaten += 1
                time_passed = time + 1
    
    return total_eaten

# Input processing
n, T = map(int, input().split())
times = list(map(int, input().split()))

# Call the function and output the result
print(max_bowls(n, T, times))
