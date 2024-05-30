
def earliest_arrival(n, m, t_a, t_b, k, departures_A, departures_B):
    if n + m <= k:
        return -1

    best_time = 0
    for cancel_a in range(min(n, k) + 1):
        cancel_b = k - cancel_a
        earliest = float('inf')

        for i in range(cancel_a, n + 1):
            min_time_a = departures_A[i - 1] + t_a if i > 0 else 0
            for j in range(cancel_b, m + 1):
                if j == 0:
                    earliest = min(earliest, min_time_a)
                elif j <= m:
                    earliest = min(earliest, max(min_time_a, departures_B[j - 1] + t_b))

        best_time = max(best_time, earliest)

    return best_time

# Input parsing
n, m, t_a, t_b, k = map(int, input().split())
departures_A = list(map(int, input().split()))
departures_B = list(map(int, input().split()))

result = earliest_arrival(n, m, t_a, t_b, k, departures_A, departures_B)
print(result)
```
