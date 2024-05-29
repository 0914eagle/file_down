
def min_coupons(N, trips):
    coupons = 0
    prev_end_zone = 0
    valid_until = 0

    for trip in trips:
        zone, time = trip
        if time > valid_until:
            # Expired ticket, need to buy a new one
            coupons += 2 + abs(prev_end_zone - zone)
            valid_until = time + 10000
            prev_end_zone = zone
        else:
            # Trip can be covered by current ticket
            prev_end_zone = zone

    return coupons

# Input processing
N = int(input())
trips = []
for _ in range(N):
    Z, T = map(int, input().split())
    trips.append((Z, T))

# Output
print(min_coupons(N, trips))
```
