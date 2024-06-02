
def min_time_to_deliver_candies(n, m, candies):
    time_needed = [0] * n
    
    for i in range(n):
        for a, b in candies:
            time = abs(i - a) + 1
            time = min(time, abs(i - b) + 1)
            time += abs(a - b)
            time_needed[i] = max(time_needed[i], time)
    
    return time_needed

# Input
n, m = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(m)]

# Output
result = min_time_to_deliver_candies(n, m, candies)
print(*result)