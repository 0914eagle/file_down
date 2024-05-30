
def earliest_arrival_time(n, m, t_a, t_b, k, departures_ab, departures_bc):
    def binary_search(departures_bc, target):
        low, high = 0, len(departures_bc) - 1
        while low <= high:
            mid = (low + high) // 2
            if departures_bc[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
    
    def feasible(time):
        canceled = 0
        j = 0
        for i in range(n):
            if j >= m:
                break
            if departures_ab[i] < time:
                continue
            while j < m and departures_bc[j] < departures_ab[i] + t_a:
                j += 1
            if j < m and departures_bc[j] < departures_ab[i] + t_a + t_b:
                canceled += 1
                if canceled > k:
                    return False
                j = binary_search(departures_bc, departures_ab[i] + t_a + t_b)
        return True
    
    departures_ab = sorted(departures_ab)
    departures_bc = sorted(departures_bc)

    left, right = departures_ab[0], departures_ab[0] + (t_a + t_b) * m
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

# Input example
n, m, t_a, t_b, k = 4, 5, 1, 1, 2
departures_ab = [1, 3, 5, 7]
departures_bc = [1, 2, 3, 9, 10]

print(earliest_arrival_time(n, m, t_a, t_b, k, departures_ab, departures_bc))
```
