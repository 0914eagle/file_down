
def earliest_arrival_time(n, m, t_a, t_b, k, depart_a, depart_b):
    def binary_search():
        left = 0
        right = k
        result = -1

        while left <= right:
            mid = (left + right) // 2
            cancel_a = mid
            cancel_b = k - mid

            if cancel_a <= n and cancel_b <= m:
                min_time = float('inf')
                for i in range(cancel_a + 1):
                    if cancel_b > 0:
                        j = min(m, cancel_b)
                        time = depart_a[i] + t_a + depart_b[j - 1] + t_b
                        min_time = min(min_time, time)
                        cancel_b -= 1
                if min_time < float('inf'):
                    result = max(result, min_time)

            if cancel_a < n and (cancel_b == m or (cancel_b < m and depart_a[cancel_a] + t_a < depart_b[cancel_b])):
                left = mid + 1
            else:
                right = mid - 1

        return result

    earliest_time = binary_search()
    return earliest_time

# Input
n, m, t_a, t_b, k = map(int, input().split())
depart_a = list(map(int, input().split()))
depart_b = list(map(int, input().split()))

# Output
result = earliest_arrival_time(n, m, t_a, t_b, k, depart_a, depart_b)
print(result)
```
