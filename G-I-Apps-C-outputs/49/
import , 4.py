
import sys

N = int(input())
trips = []
for _ in range(N):
    Z, T = map(int, input().split())
    trips.append((Z, T))

coupons = 0
valid_ticket = None

for zone, time in trips:
    if valid_ticket and time >= valid_ticket[1]:
        coupons += 2 + abs(zone - valid_ticket[0])
        valid_ticket = (zone, time + 10000)
    else:
        valid_ticket = (zone, time + 10000)

print(coupons)
```
