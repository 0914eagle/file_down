
def min_time_to_deliver(n, m, candies):
    time_needed = [0] * n
    
    for i in range(n):
        for a, b in candies:
            time = abs(i - a) + 1
            time += min(abs(a - b), n - abs(a - b))
            time += abs(b - i) + 1
            time_needed[i] += time
    
    return time_needed

# Input
n, m = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(m)]

# Output
result = min_time_to_deliver(n, m, candies)
print(*result)
