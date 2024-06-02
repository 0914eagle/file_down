
def min_delivery_time(n, m, candies):
    delivery_times = [0] * n
    
    for i in range(n):
        for a, b in candies:
            time = abs(i - a) + 1
            time += abs(a - b) if a <= b else n - a + b
            delivery_times[i] = max(delivery_times[i], time)
    
    return delivery_times

# Input parsing
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
result = min_delivery_time(n, m, candies)
print(*result)
