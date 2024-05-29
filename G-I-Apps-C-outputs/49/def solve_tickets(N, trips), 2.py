
import heapq

def solve_tickets(N, trips):
    coupons = 0
    valid_tickets = []
    current_zone = 0

    for zone, time in trips:
        while valid_tickets and valid_tickets[0][0][1] < time:
            heapq.heappop(valid_tickets)
        
        min_coupons = float('inf')
        for ticket in valid_tickets:
            min_coupons = min(min_coupons, ticket[1])
        
        if not valid_tickets or min_coupons > 2 + abs(zone - current_zone):
            heapq.heappush(valid_tickets, ((min(zone, current_zone), max(zone, current_zone)), 2 + abs(zone - current_zone)))
            coupons += 2 + abs(zone - current_zone)
            current_zone = zone
        
    return coupons

# Input parsing
N = int(input())
trips = []
for _ in range(N):
    zone, time = map(int, input().split())
    trips.append((zone, time))

# Call the function and print the result
print(solve_tickets(N, trips))
```
