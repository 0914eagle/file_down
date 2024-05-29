
def min_coupons(N, trips):
    coupons = 0
    current_ticket = None

    for i in range(N):
        zone, time = trips[i]

        if current_ticket is None or time > current_ticket[1] + 10000 or not current_ticket[0][0] <= zone <= current_ticket[0][1]:
            # Buy a new ticket
            if current_ticket is not None:
                coupons += 2 + abs(zone - current_ticket[0][0])
            current_ticket = ((zone, zone), time)
        else:
            current_ticket = ((min(current_ticket[0][0], zone), max(current_ticket[0][1], zone)), current_ticket[1])

    return coupons

# Read input
N = int(input())
trips = []
for i in range(N):
    zone, time = map(int, input().split())
    trips.append((zone, time))

result = min_coupons(N, trips)
print(result)
```
