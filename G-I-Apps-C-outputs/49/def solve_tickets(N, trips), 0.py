
import heapq

def solve_tickets(N, trips):
    tickets = []
    total_coupons = 0

    for zone, time in trips:
        while tickets and tickets[0][0] < time:
            heapq.heappop(tickets)

        if not tickets or zone < tickets[0][1][0] or zone > tickets[0][1][1]:
            new_ticket_zone = (zone, zone)
            heapq.heappush(tickets, (time + 10000, new_ticket_zone))
            total_coupons += 2
        else:
            new_ticket_zone = tickets[0][1]

        heapq.heappush(tickets, (time + 10000, new_ticket_zone))

    return total_coupons

# Read input
N = int(input())
trips = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
print(solve_tickets(N, trips))
```
