
def arrival_time(n, m, t_a, t_b, k, departures_ab, departures_bc):
    def possible(arrival_time):
        cnt = 0
        j = 0
        for i in range(n):
            while j < m and departures_bc[j] < arrival_time:
                j += 1
            if j == m:
                return False
            if departures_bc[j] >= departures_ab[i] + t_a:
                j += 1
            else:
                cnt += 1
            if cnt > k:
                return False
        return True

    left = t_a * n
    right = 10**18
    while left < right:
        mid = (left + right) // 2
        if possible(mid):
            right = mid
        else:
            left = mid + 1

    if right == 10**18:
        return -1
    return right

n, m, t_a, t_b, k = map(int, input().split())
departures_ab = list(map(int, input().split()))
departures_bc = list(map(int, input().split())

result = arrival_time(n, m, t_a, t_b, k, departures_ab, departures_bc)
print(result)
```
