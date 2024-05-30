
def earliest_arrival_time(n, m, t_a, t_b, k, departures_a, departures_b):
    def find_optimal_arrival():
        left, right = 0, 10**18
        while left < right:
            mid = (left + right) // 2
            count = 0
            j = 0
            for i in range(n):
                while j < m and departures_a[i] + t_a + mid > departures_b[j]:
                    j += 1
                count += max(0, j - i - k)
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left if left < 10**18 else -1

    departures_a.sort()
    departures_b.sort()

    return find_optimal_arrival()

# Input parsing
n, m, t_a, t_b, k = map(int, input().split())
departures_a = list(map(int, input().split()))
departures_b = list(map(int, input().split()))

# Call the function and output the result
result = earliest_arrival_time(n, m, t_a, t_b, k, departures_a, departures_b)
print(result)
```
