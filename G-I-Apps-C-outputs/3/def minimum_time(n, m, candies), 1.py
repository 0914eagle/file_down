
def minimum_time(n, m, candies):
    time_list = []
    for i in range(1, n + 1):
        time = 0
        for candy in candies:
            a, b = candy
            time += min(abs(i - a), n - abs(i - a)) + min(abs(a - b), n - abs(a - b))
        time_list.append(time)
    return time_list

# Input
n, m = map(int, input().split())
candies = []
for _ in range(m):
    a, b = map(int, input().split())
    candies.append((a, b))

# Output
result = minimum_time(n, m, candies)
print(*result)
```
