
def solve_tickets(N, trips):
    coupons = 0
    current_zone = 0
    valid_until = 0
    
    for i in range(N):
        zone, time = trips[i]
        diff = abs(zone - current_zone)
        if time > valid_until:
            coupons += 2 + diff
            valid_until = time + 10000
        else:
            if diff > 0:
                coupons += 2 + diff
            valid_until = max(valid_until, time + 10000)
        current_zone = zone
        
    return coupons

# Reading input
N = int(input())
trips = []
for _ in range(N):
    zone, time = map(int, input().split())
    trips.append((zone, time))

# Calling the function and printing the result
print(solve_tickets(N, trips))
```
