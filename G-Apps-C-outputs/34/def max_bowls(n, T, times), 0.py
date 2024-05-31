
def max_bowls(n, T, times):
    eaten = 0
    current_time = 0
    for i in range(n):
        if current_time + times[i] <= T:
            eaten += 1
            current_time += times[i]
        else:
            break
    return eaten

# Input processing
n, T = map(int, input().split())
times = list(map(int, input().split()))

# Call the function and output the result
result = max_bowls(n, T, times)
print(result)
