
def min_time_to_deliver(n, m, candies):
    def find_time(start):
        time = 0
        for i in range(m):
            a_i, b_i = candies[i]
            time += min((b_i - a_i) % n, (a_i - b_i) % n) + 1
        return time

    ans = []
    for i in range(1, n+1):
        ans.append(find_time(i))

    return ans

# Input processing
n, m = map(int, input().split())
candies = []
for _ in range(m):
    a_i, b_i = map(int, input().split())
    candies.append((a_i, b_i))

# Calculate minimum time for each station
result = min_time_to_deliver(n, m, candies)

# Output the result
print(" ".join(map(str, result)))
```
