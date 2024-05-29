
def minimize_coupons(N, trips):
    current_zone = 0
    current_ticket = None
    coupons_needed = 0

    for i in range(N):
        zone, time = trips[i]

        if current_ticket is None or time > current_ticket[2]:
            # Need to buy a new ticket
            if current_ticket is not None:
                coupons_needed += current_ticket[1] # Add coupons for the previous ticket
            current_ticket = (zone, abs(current_zone - zone) + 2, time + 10000)

        current_zone = zone

    coupons_needed += current_ticket[1] # Add coupons for the last ticket
    return coupons_needed

# Input parsing
N = int(input())
trips = []
for _ in range(N):
    Z, T = map(int, input().split())
    trips.append((Z, T))

# Call the function and output the result
print(minimize_coupons(N, trips))
```
