
import bisect

def find_earliest_arrival(n, m, t_a, t_b, k, depart_a, depart_b):
    INF = 10**18
    l = 0
    r = INF

    while l < r:
        mid = (l + r + 1) // 2
        cnt = 0
        j = 0

        for i in range(n):
            while j < m and depart_b[j] < depart_a[i] + t_a:
                j += 1
            if j >= m or depart_b[j] - depart_a[i] - t_a > mid:
                cnt += 1
            if cnt > k:
                break
                
        if cnt <= k:
            l = mid
        else:
            r = mid - 1

    if l == INF:
        return -1
    return max(depart_a[-1] + t_a, depart_b[bisect.bisect_right(depart_b, l) - 1] + t_b)

# Input parsing
n, m, t_a, t_b, k = map(int, input().split())
depart_a = list(map(int, input().split()))
depart_b = list(map(int, input().split()))

# Call the function with the given inputs and print the result
print(find_earliest_arrival(n, m, t_a, t_b, k, depart_a, depart_b))
```
