
def min_coupons(N, trips):
    interval = [0, 0]
    total_coupons = 0
    for i in range(N):
        zone, time = trips[i]
        while interval[1] - time < 0:
            interval[0], interval[1] = zone, zone
            total_coupons += 2
        if zone < interval[0]:
            total_coupons += interval[0] - zone
            interval[0] = zone
        elif zone > interval[1]:
            total_coupons += zone - interval[1]
            interval[1] = zone
    return total_coupons

# Reading input
N = int(input())
trips = [list(map(int, input().split())) for _ in range(N)]

# Calling the function and printing the result
print(min_coupons(N, trips))
```
